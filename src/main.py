import sys
import json

from src.config import ConfigError

try:
    from src.config import GROQ_API_KEY, STT_MODEL, LLM_MODEL
    from src.transcription import transcribe
    from src.summary import generate_summary
except ConfigError as e:
    print(f"Erreur de configuration: {e}")
    sys.exit(1)


def main():
    audio_path = "audios/demo.mp4"

    try:
        transcription = transcribe(audio_path)
    except FileNotFoundError:
        print(f"Erreur: fichier audio introuvable ({audio_path})")
        sys.exit(1)
    except Exception as e:
        print(f"Erreur lors de la transcription: {e}")
        sys.exit(1)

    try:
        summary = generate_summary(transcription.text)
    except Exception as e:
        print(f"Erreur lors de la génération du résumé: {e}")
        sys.exit(1)

    try:
        result = json.loads(summary)
    except json.JSONDecodeError:
        print("Erreur: le résumé retourné n'est pas un JSON valide")
        print(summary)
        sys.exit(1)

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
