from pypdf import PdfReader, PdfWriter
import time
import sys
import os


class pdfiy:
    def __init__(self, files) -> None:
        self.writer = PdfWriter()
        self.files = files
        pass
    
    def mkdir(self, dir_name):
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
            return True
        return False

    def check_if_pdf(self, file_ext):
        if file_ext == ".pdf":
            return True
        return False

    def merge(self):
        file_name = ""
        for file in files:
            file_list = os.path.splitext(file)
            file_name = os.path.basename(file_list[0])
            file_ext = file_list[-1]
            if not os.path.exists(file):
                # nofity
                print(f"File does not exist: {file}")
                continue
            if not self.check_if_pdf(file_ext):
                # nofity
                print("Please provide a valid PDF file.") 
                continue
            self.writer.append(file)
        nowtime = time.strftime("%Y-%m-%d_%H.%M.%S", time.localtime(time.time()))
        self.writer.write(f"{file_name}-merged-{nowtime}.pdf")
        self.writer.close()

    def split(self, input_file, file_name, output_dir):
        pdf = PdfReader(open(input_file, "rb"))
        for page_index in range(len(pdf.pages)):
            writer = PdfWriter()
            writer.add_page(pdf.pages[page_index])
            output_pdf_name = f"{output_dir}/{file_name}-page-{page_index+1}.pdf"
            with open(output_pdf_name, 'wb') as output_file:
                writer.write(output_file)

    def split_execute(self):
        if len(self.files) == 0:
            # nofity
            print("Please provide a PDF file.")
            sys.exit(1)
        for file in files:
            if not os.path.exists(file):
                print(f"File does not exist: {file}")
                # nofity
                sys.exit(1)      
            file_list = os.path.splitext(file)
            dir_name = file_list[0]
            file_name = os.path.basename(file_list[0])
            file_ext = file_list[-1]       
            if self.check_if_pdf(file_ext):
                # nofity
                print("Please provide a valid PDF file.")
                continue
            nowtime = time.strftime("%Y-%m-%d_%H.%M.%S", time.localtime(time.time()))
            output_dir = f"{dir_name}-splitted-{nowtime}"
            self.mkdir(output_dir)
            self.split(file, file_name, output_dir)


if __name__ == "__main__":
    files = sys.argv[2:]
    op = sys.argv[1]

    if len(files) == 0:
        # nofity
        print("Please provide at least one  PDF file.")
        sys.exit(1)

    if op == "merge":
        pdfiy(files).merge()
    elif op == "split":
        pdfiy(files).split_execute()
    else:
        # nofity
        print("Please provide a valid operation.")
    pass