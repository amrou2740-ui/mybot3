from gemini_client import safe_generate

class WriterAgent:

    def __init__(self, api_key):
        self.api_key = api_key

    def write(self, title, context):

        prompt = f'''
اكتب فصل أكاديمي احترافي بعنوان:

{title}

اعتماداً على المعلومات التالية:

{context}

ويجب أن يكون:
- منظم
- أكاديمي
- واضح
- طويل نسبياً
'''

        return safe_generate(prompt)