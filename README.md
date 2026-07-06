# scribe

Un petit outil en ligne de commande qui transforme un enregistrement audio (une réunion, un cours, une note vocale) en compte rendu écrit et structuré.
Son fonctionnement tient en trois temps :

1. L'utilisateur fournit un fichier audio.
2. Un modèle de transcription (Speech-to-Text) convertit l'audio en texte brut.
3. Un LLM reformule ce texte brut en compte rendu propre : titre, points clés, décisions, actions à
   mener

## Modèles Groq choisis

### STT — whisper-large-v3-turbo

Groq propose deux variantes Whisper : whisper-large-v3 et whisper-large-v3-turbo.

On choisit la Turbo :

Vitesse : ~228× temps réel (une heure d'audio transcrite en ~15s), contre un ratio plus faible pour la v3 classique.
Coût : $0.04/heure d'audio, contre un tarif plus élevé pour la v3 standard.

Qualité : Précision baisse par rapport à la v3 classique, mais négligeable pour des notes qu'on teste pour notre projet.

LLM — openai/gpt-oss-120b

Groq a déprécié llama-3.3-70b-versatile et llama-3.1-8b-instant en juin 2026, migration recommandée vers openai/gpt-oss-120b (ou gpt-oss-20b ou aussi qwen/qwen3.6-27b

On choisit le 120B :

Qualité : contexte 131k tokens, largement suffisant pour notre projet ; meilleure capacité de synthèse structurée que le 20B.
Vitesse : ~500 tokens/s sur l'infrastructure LPU de Groq, adapté à un usage CLI interactif.
Coût : $0.15 / $0.60 par million de tokens (entrée/sortie), avec cache de prompt à $0.075 sur l'entrée

# Q3: Reponse model

Avec response_format="verbose_json", l'objet Transcription retourné contient, en plus de text :

language - langue détectée automatiquement.
duration - durée totale de l'audio en secondes (228.74s sur notre exemple).
segments - liste de blocs découpant la transcription dans le temps, chacun avec :

start / end - horodatage précis du segment (ex : segment 18 va de 105.38s à 122.29s).
avg_logprob — confiance moyenne du modèle sur ce segment (proche de 0 = confiant, très négatif = incertain).
Sur notre test, le segment 24 ("télé expertise") tombe à -0.45, contre -0.15 pour un segment bien capté.
no_speech_prob — probabilité qu'il n'y ait pas de parole (silence). Toujours à 0 ici, audio continu sans blanc.
compression_ratio — ratio texte/tokens, un indicateur indirect de répétition ou de bruit dans la transcription.
tokens — les tokens bruts du modèle (peu utile en l'état, sert au debug interne).

x_groq.id — identifiant de requête côté Groq, utile pour du support/debug.
