from pypdf import PdfReader, PdfWriter
import os
import time

writer = PdfWriter()

def create_dir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        return True
    return False

def check_if_pdf(file_ext):
    if os.path.splitext(file_ext) == ".pdf":
        return True
    return False

def split_pdf(input_pdf_path, output_dir):
    input_pdf_file = PdfReader(open(input_pdf_path, "rb"))

    for page_index in range(len(input_pdf_file.pages)):
        writer.add_page(input_pdf_file.pages[page_index])

        output_pdf_name = input_pdf_path.split(".pdf")[0] + f"-{page_index+1}" + '.pdf'

        with open(output_pdf_name, 'wb') as output_pdf_file:
            writer.write(output_pdf_file)


if __name__ == "__main__":

    file = "C:/Users/ismail/dev/side-projects/pdf-merge-split/pdf-1.pdf"
    file = file.strip()

    file_list = os.path.splitext(file)

    dir_name = file_list[0]
    file_name = os.path.basename(file_list[0])
    file_ext = file_list[-1]

    if check_if_pdf(file_ext):
        nowtime = time.strftime("%Y-%m-%d_%H.%M.%S", time.localtime(time.time()))
        output_dir = dir_name + f"-{nowtime}"

        create_dir(output_dir)
        split_pdf(file, output_dir)
    else:
        print("Please provide a valid PDF file.")