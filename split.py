from pypdf import PdfReader, PdfWriter
import os

writer = PdfWriter()

def check_if_pdf(input_file):
    if os.path.splitext(input_file) == ".pdf":
        return True
    return False

def split_pdf(input_pdf_name):
    input_pdf_file = PdfReader(open(input_pdf_name, "rb"))

    for page_index in range(len(input_pdf_file.pages)):
        writer.add_page(input_pdf_file.pages[page_index])

        output_pdf_name = input_pdf_name.split(".pdf")[0] + f"-{page_index+1}" + '.pdf'

        with open(output_pdf_name, 'wb') as output_pdf_file:
            writer.write(output_pdf_file)


if __name__ == "__main__":
    
    input_pdf_name = "pdf-1.pdf"

    if check_if_pdf(input_pdf_name):
        split_pdf(input_pdf_name)
    else:
        print("Please provide a valid PDF file.")