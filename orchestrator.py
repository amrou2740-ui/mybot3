import json
import os

from config import GEMINI_API_KEY, OUTPUT_DIR

from agents.strategist import StrategistAgent
from agents.researcher import ResearcherAgent
from agents.writer import WriterAgent
from agents.data_viz import DataVizAgent
from agents.compiler import CompilerAgent

os.makedirs(OUTPUT_DIR, exist_ok=True)

async def run_thesis_pipeline(topic, cb=None):

    async def update(step, total, text):

        progress = f"📊 [{step}/{total}] {text}"

        print(progress)

        if cb:
            await cb(progress)

    TOTAL = 5

    await update(1, TOTAL, "تحليل الموضوع وإنشاء الخطة...")

    strategist = StrategistAgent()
    outline_raw = strategist.create_outline(topic)

    try:
        outline = json.loads(outline_raw)

        if "chapters" not in outline:
            raise Exception()

    except Exception:
        outline = {
            "chapters": [
                {"title": "المقدمة"},
                {"title": "الإطار النظري"},
                {"title": "التحليل"},
                {"title": "الخاتمة"}
            ]
        }

    await update(2, TOTAL, "جمع المصادر والمعلومات الأكاديمية...")

    researcher = ResearcherAgent(GEMINI_API_KEY)
    research_data = researcher.gather(topic)

    await update(3, TOTAL, "كتابة الفصول العلمية...")

    writer = WriterAgent(GEMINI_API_KEY)

    chapters = {}

    for chapter in outline["chapters"]:

        title = chapter["title"]

        await update(3, TOTAL, f"كتابة فصل: {title}")

        chapters[title] = writer.write(
            title,
            research_data["summary"]
        )

    await update(4, TOTAL, "إنشاء الرسوم البيانية...")

    viz = DataVizAgent()
    images = viz.make(topic, OUTPUT_DIR)

    await update(5, TOTAL, "تجميع ملف PDF النهائي...")

    compiler = CompilerAgent()

    pdf_path = compiler.build(
        chapters,
        images,
        OUTPUT_DIR
    )

    await update(5, TOTAL, "اكتمل المشروع بنجاح ✅")

    return {
        "pdf_path": pdf_path
    }