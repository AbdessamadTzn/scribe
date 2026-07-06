import os
from dotenv import load_dotenv

load_dotenv()


class ConfigError(Exception):
    """Erreur de configuration"""
    pass


GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ConfigError("GROQ_API_KEY manquante.")

STT_MODEL = "whisper-large-v3-turbo"
LLM_MODEL = "openai/gpt-oss-120b"