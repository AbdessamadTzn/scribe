import sys
import json
from datetime import datetime
from pathlib import Path

from src.config import ConfigError

try:
    from src.config import GROQ_API_KEY, STT_MODEL, LLM_MODEL
    from src.transcription import transcribe
    from src.summary import generate_summary
except ConfigError as e:
    print(f"Erreur de configuration: {e}")
    sys.exit(1)

OUTPUT_DIR = Path("comptes_rendus")


def to_markdown(data: dict) -> str:
    points_cles = "\n".join(f"- {p}" for p in data.get("points_cles", []))
    decisions = "\n".join(f"- {d}" for d in data.get("decisions_et_actions", []))

    return (
        f"# {data.get('titre', 'Compte rendu')}\n\n"
        f"## Résumé\n{data.get('resume', '')}\n\n"
        f"## Points clés\n{points_cles}\n\n"
        f"## Décisions et actions\n{decisions}\n"
    )


def main():
    audio_path = sys.argv[1]

    print("Transcription en cours...")
    try:
        transcription = transcribe(audio_path)
    except FileNotFoundError:
        print(f"Erreur: fichier audio introuvable ({audio_path})")
        sys.exit(1)
    except Exception as e:
        print(f"Erreur lors de la transcription: {e}")
        sys.exit(1)

    print("Rédaction du compte rendu en cours...")
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

    markdown = to_markdown(result)
    print(markdown)

    OUTPUT_DIR.mkdir(exist_ok=True)
    output_path = OUTPUT_DIR / f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.md"
    output_path.write_text(markdown, encoding="utf-8")
    print(f"Compte rendu sauvegardé dans {output_path}")


if __name__ == "__main__":
    main()

