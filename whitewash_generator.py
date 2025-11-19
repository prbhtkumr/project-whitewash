import random
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.colors import Color

def draw_foia_stamp(c, x, y):
    stamp_color = Color(0.2, 0.2, 0.2, alpha=0.9)

    c.saveState()
    c.translate(x, y)
    rotation = random.uniform(-5, 5)
    c.rotate(rotation)

    c.setStrokeColor(stamp_color)
    c.setFillColor(stamp_color)
    c.setLineWidth(2)
    c.setFont("Courier-Bold", 14)

    c.rect(-10, -8, 240, 32, fill=0, stroke=1)

    c.drawString(0, 5, "RELEASED PER FOIA REQUEST")

    c.restoreState()

def create_redacted_pdf(filename="epstein_list_release_final_v2_DO_NOT_OPEN.pdf"):
    c = canvas.Canvas(filename, pagesize=LETTER)

    c.setTitle("Epstein List SATIRE")
    c.setAuthor("Project WHITEWASH Generator by Prabhat Kumar")
    c.setSubject("This is a satirical document containing randomly generated patterns. It is not a real government record.")
    c.setKeywords(["Satire", "Parody", "Epstein", "Redacted", "Fake", "Humor"])
    c.setCreator("Python ReportLab - Satire Tool")

    width, height = LETTER

    margin = 1 * inch
    top_margin = height - 1 * inch
    bottom_margin = 1 * inch
    line_height = 14
    word_spacing = 6
    paragraph_spacing = 20

    font_name = "Courier"
    font_size = 12

    target_word = "Epstein"
    mention_probability = 0.02

    scanned_text_color = Color(0.15, 0.15, 0.15)

    redaction_color = Color(0, 0, 0)

    total_pages = 97

    print(f"Generating {total_pages} pages of classified obfuscation...")

    for page_num in range(1, total_pages + 1):
        c.saveState()
        c.setFont("Helvetica-Bold", 85)
        c.setFillColorRGB(1, 0, 0)
        c.setFillAlpha(0.2)
        c.translate(width / 2, height / 2)
        c.rotate(45)
        c.drawCentredString(0, 0, "CLASSIFIED")
        c.restoreState()

        draw_foia_stamp(c, width - 3.5 * inch, height - 0.8 * inch)

        if page_num > 1 and random.random() < 0.05:
            c.setFont("Courier-Bold", 12)
            c.setFillColor(scanned_text_color)
            c.drawCentredString(width / 2, height / 2, "[THIS PAGE INTENTIONALLY LEFT BLANK]")
            c.setFont("Courier", 10)
            c.drawString(width - margin, margin / 2, f"Page {page_num}")
            c.showPage()
            continue

        current_y = top_margin

        if page_num == 1:
            c.setFont("Courier-Bold", 24)
            c.setFillColor(scanned_text_color)
            c.drawCentredString(width / 2, top_margin - 0.5*inch, "SUBJECT: THE EPSTEIN LIST")
            c.setFont("Courier", 10)
            c.drawCentredString(width / 2, top_margin - 0.8*inch, "DOJ / EXHIBIT A / UNSEALED")
            c.setFont(font_name, font_size)
            current_y -= 1.5 * inch
        else:
            c.setFont(font_name, font_size)

        while True:
            lines_in_paragraph = random.randint(3, 12)
            para_height = (lines_in_paragraph * line_height) + paragraph_spacing

            if current_y - para_height < bottom_margin:
                break

            for line_idx in range(lines_in_paragraph):
                current_x = margin
                max_x = width - margin

                while current_x < max_x:
                    is_target = random.random() < mention_probability

                    if is_target:
                        c.setFillColor(scanned_text_color)
                        text_width = c.stringWidth(target_word, font_name, font_size)

                        if current_x + text_width > max_x:
                            break

                        c.drawString(current_x, current_y, target_word)
                        current_x += text_width + word_spacing
                    else:
                        c.setFillColor(redaction_color)
                        word_width = random.randint(20, 80)

                        if current_x + word_width > max_x:
                            break

                        c.rect(current_x, current_y - 3, word_width, 12, fill=1, stroke=0)

                        current_x += word_width + word_spacing

                current_y -= line_height

            current_y -= paragraph_spacing

        c.setFillColor(scanned_text_color)
        c.setFont("Courier", 10)
        c.drawString(width - margin - 0.5*inch, margin / 2, f"Page {page_num}")

        c.showPage()

    c.save()
    print(f"SUCCESS. Document saved to: {filename}")

if __name__ == "__main__":
    create_redacted_pdf()
