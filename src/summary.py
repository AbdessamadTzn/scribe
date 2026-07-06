import json
from pathlib import Path
from groq import Groq
from src.config import LLM_MODEL
client = Groq()

PROMPT_PATH = Path(__file__).parent.parent / "prompts" / "system_prompt.txt"


def generate_summary(transcription_text: str) -> str:

    with open(PROMPT_PATH, "r", encoding="utf-8") as f:
        system_prompt = f.read()

    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": transcription_text},
        ],
        temperature=0.2,
        response_format={"type": "json_object"},
    )

    return response.choices[0].message.content
