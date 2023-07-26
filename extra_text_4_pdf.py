from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import PyPDF2
import fitz


# def extract_text_from_pdf(file_path):
#     with open(file_path, 'rb') as file:
#         reader = PyPDF2.PdfReader(file)
#         text = ''
#         for page in reader.pages:
#             text += page.extract_text()
#     return text


def extract_text_from_pdf(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text


def extract_text_from_pdf_by_pdfminer(file_path):
    resource_manager = PDFResourceManager()
    output_string = StringIO()
    laparams = LAParams()
    text_converter = TextConverter(resource_manager, output_string, laparams=laparams)
    with open(file_path, 'rb') as file:
        interpreter = PDFPageInterpreter(resource_manager, text_converter)
        for page in PDFPage.get_pages(file, check_extractable=True):
            interpreter.process_page(page)
        text = output_string.getvalue()
    text_converter.close()
    output_string.close()
    return text


def extract_text_from_pdf_by_pymupdf(file_path):
    text = ''
    doc = fitz.open(file_path)
    for page in doc:
        text += page.get_text("text")
    return text


def main():
    path = 'D:/Document/pro/pro-depot invoice template.pdf'
    option = int(input("Please enter an integer value (1, 2, 3): "))
    if option == 1:
        pdf_text = extract_text_from_pdf(path)
    elif option == 2:
        pdf_text = extract_text_from_pdf_by_pdfminer(path)
    elif option == 3:
        pdf_text = extract_text_from_pdf_by_pymupdf(path)
    else:
        print("Invalid input")
        pdf_text = ''

    print(pdf_text)


if __name__ == '__main__':
    main()
