import sys
from src.config import ConfigError

try:
    from src.config import GROQ_API_KEY, STT_MODEL, LLM_MODEL
except ConfigError as e:
    print(f"Erreur {e}")
    sys.exit(1)
