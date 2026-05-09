import google.generativeai as genai
from config import GEMINI_API_KEY, GEMINI_MODEL

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(
    model_name=GEMINI_MODEL,
    generation_config={
        "temperature": 0.7,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
    }
)

def safe_generate(prompt, retries=3):
    for attempt in range(retries):
        try:
            response = model.generate_content(prompt)

            if hasattr(response, "text"):
                return response.text.strip()

            return "لم يتم إرجاع نص"

        except Exception as e:
            print(f"Gemini Error: {e}")

            if attempt == retries - 1:
                return f"خطأ Gemini: {str(e)}"