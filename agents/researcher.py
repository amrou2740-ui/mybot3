from gemini_client import safe_generate

class ResearcherAgent:

    def __init__(self, api_key):
        self.api_key = api_key

    def gather(self, topic):

        prompt = f'''
اكتب معلومات أكاديمية مفصلة عن:

{topic}

ويجب أن تتضمن:
- مقدمة
- شرح علمي
- أمثلة
- تطبيقات
- خاتمة
'''

        return {
            "summary": safe_generate(prompt)
        }