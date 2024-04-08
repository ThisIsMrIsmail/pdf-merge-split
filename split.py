from pypdf import PdfReader, PdfWriter
import os
import sys
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
        writer = PdfWriter()
        writer.add_page(pdf.pages[page_index])

        output_pdf_name = f"{output_dir}/{file_name}-page-{page_index+1}.pdf"

        with open(output_pdf_name, 'wb') as output_file:
            writer.write(output_file)


if __name__ == "__main__":

    # file = f"{os.path.expanduser("~")}/dev/side-projects/pdfiy/pdf-1.pdf"
    # file = file.strip()

    files = sys.argv[1:]

    if len(files) == 0:
        print("Please provide a PDF file.")
        sys.exit(1)
    
    for file in files:
        if not os.path.exists(file):
            print(f"File does not exist: {file}")
            time.sleep(3)
            sys.exit(1)
        
        file_list = os.path.splitext(file)

        dir_name = file_list[0]
        file_name = os.path.basename(file_list[0])
        file_ext = file_list[-1]
        
        if check_if_pdf(file_ext):
            nowtime = time.strftime("%Y-%m-%d_%H.%M.%S", time.localtime(time.time()))
            output_dir = dir_name + f"-splitted-{nowtime}"

            create_dir(output_dir)
            split_pdf(file, file_name, output_dir)
        else:
            print("Please provide a valid PDF file.")