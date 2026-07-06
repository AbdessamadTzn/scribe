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
