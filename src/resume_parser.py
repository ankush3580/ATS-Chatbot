from pypdf import PdfReader


def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF resume.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Extracted text from all PDF pages.
    """
    reader = PdfReader(pdf_path)

    text = []

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text.append(page_text)

    return "\n".join(text)


if __name__ == "__main__":
    print("Resume parser module loaded successfully.")