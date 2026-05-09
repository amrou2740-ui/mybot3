from gemini_client import safe_generate

class StrategistAgent:

    def create_outline(self, topic):

        prompt = f'''
أنشئ خطة بحث أكاديمية احترافية بصيغة JSON فقط.

الشكل المطلوب:

{{
  "chapters": [
    {{"title": "..."}},
    {{"title": "..."}}
  ]
}}

الموضوع:
{topic}
'''

        return safe_generate(prompt)