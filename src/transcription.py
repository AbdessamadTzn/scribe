import json
from groq import Groq
from src.config import STT_MODEL


client = Groq()

filename = "audios/demo.mp4"


with open(filename, "rb") as file:

    transcription = client.audio.transcriptions.create(
        file=file,
        model=STT_MODEL,
        response_format="verbose_json",
        language="fr",
        temperature=0.0,
    )
    print(json.dumps(transcription, indent=2, default=str))