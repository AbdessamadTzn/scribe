from groq import Groq
from src.config import STT_MODEL


client = Groq()


def transcribe(filename: str):
    with open(filename, "rb") as file:
        return client.audio.transcriptions.create(
            file=file,
            model=STT_MODEL,
            response_format="verbose_json",
            language="fr",
            temperature=0.0,
        )
