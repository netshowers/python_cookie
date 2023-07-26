from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO


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


def main():
    path = 'D:/Document/pro/pro-depot invoice template.pdf'
    pdf_text = extract_text_from_pdf_by_pdfminer(path)
    print(pdf_text)


if __name__ == '__main__':
    main()
