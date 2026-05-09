from fpdf import FPDF
import os
import arabic_reshaper
from bidi.algorithm import get_display

class CompilerAgent:

    def arabic(self, text):

        reshaped = arabic_reshaper.reshape(text)

        return get_display(reshaped)

    def build(self, chapters, images, output_dir):

        pdf = FPDF()

        pdf.set_auto_page_break(auto=True, margin=15)

        pdf.add_font(
            "DejaVu",
            "",
            "fonts/DejaVuSans.ttf"
        )

        pdf.add_page()

        pdf.set_font("DejaVu", size=18)

        title = self.arabic("بحث أكاديمي")

        pdf.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT", align="C")

        pdf.ln(10)

        for chapter_title, content in chapters.items():

            pdf.set_font("DejaVu", size=16)

            pdf.multi_cell(
                0,
                10,
                self.arabic(chapter_title)
            )

            pdf.ln(3)

            pdf.set_font("DejaVu", size=12)

            pdf.multi_cell(
                0,
                8,
                self.arabic(content)
            )

            pdf.ln(10)

        for img in images:

            pdf.add_page()

            pdf.image(img, w=180)

        path = os.path.join(output_dir, "thesis.pdf")

        pdf.output(path)

        return path