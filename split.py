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
    if file_ext == ".pdf":
        return True
    return False

def split_pdf(input_file, file_name, output_dir):
    pdf = PdfReader(open(input_file, "rb"))

    for page_index in range(len(pdf.pages)):
        writer.add_page(pdf.pages[page_index])

        output_pdf_name = output_dir + file_name + f"-page-{page_index+1}" + '.pdf'

        with open(output_pdf_name, 'wb') as output_file:
            writer.write(output_file)


if __name__ == "__main__":

    file = "C:/Users/ismail/dev/side-projects/pdf-merge-split/pdf-1.pdf"
    file = file.strip()

    file_list = os.path.splitext(file)

    dir_name = file_list[0]
    file_name = os.path.basename(file_list[0])
    file_ext = file_list[-1]
    
    print(file_list)
    print(dir_name)
    print(file_name)
    print(file_ext)


    if check_if_pdf(file_ext):
        nowtime = time.strftime("%Y-%m-%d_%H.%M.%S", time.localtime(time.time()))
        output_dir = dir_name + f"-{nowtime}"

        create_dir(output_dir)
        split_pdf(file, file_name, output_dir)
    else:
        print("Please provide a valid PDF file.")