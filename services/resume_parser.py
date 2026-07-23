import fitz
from docx import Document


def extract_pdf_text(file_path):
    """
    Extract text from a PDF file.
    """

    text = ""

    pdf = fitz.open(file_path)

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text


def extract_docx_text(file_path):
    """
    Extract text from a DOCX file.
    """

    doc = Document(file_path)

    text = ""

    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"

    return text


def extract_resume_text(file_path):
    """
    Automatically detect the file type
    and extract text.
    """

    if file_path.endswith(".pdf"):
        return extract_pdf_text(file_path)

    elif file_path.endswith(".docx"):
        return extract_docx_text(file_path)

    else:
        raise ValueError("Unsupported file format.")