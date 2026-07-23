from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

def create_resume_pdf(text, filename="generated_resume.pdf"):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    for line in text.split("\n"):

        if line.strip():
            story.append(Paragraph(line, styles["BodyText"]))

    doc.build(story)

    return filename