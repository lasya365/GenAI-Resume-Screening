#resume_parser.py
import pdfplumber


def extract_resume_text(pdf_path):
    """
    Extract text from uploaded resume PDF
    """

    text = ""

    try:
        with pdfplumber.open(pdf_path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        return text

    except Exception as e:
        return f"Error reading PDF: {str(e)}"


if __name__ == "__main__":

    pdf_file = input("Enter PDF file path: ")

    text = extract_resume_text(pdf_file)

    print(text[:1000])