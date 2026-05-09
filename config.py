import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "PUT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "PUT_KEY")

GEMINI_MODEL = "gemini-2.5-flash"

OUTPUT_DIR = "output"