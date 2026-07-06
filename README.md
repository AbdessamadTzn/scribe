# scribe

Un petit outil en ligne de commande qui transforme un enregistrement audio (une réunion, un cours, une note vocale) en compte rendu écrit et structuré.
Son fonctionnement tient en trois temps :

1. L'utilisateur fournit un fichier audio.
2. Un modèle de transcription (Speech-to-Text) convertit l'audio en texte brut.
3. Un LLM reformule ce texte brut en compte rendu propre : titre, points clés, décisions, actions à
   mener
