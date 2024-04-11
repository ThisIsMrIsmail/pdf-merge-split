from pypdf import PdfReader, PdfWriter
import tkinter as tk
import tkinter.messagebox
import time
import sys
import os


class pdfiy:
    def __init__(self, files):
        self.writer = PdfWriter()
        self.files = files
        pass
    
    def notify(self, msg):
        window = tk.Tk()
        window.iconbitmap("pdfiy.ico")
        window.mainloop()
        tkinter.messagebox.showerror(title="PDFIY", message=msg, icon="warning", type="ok")

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
        first_file = self.files[0]
        dir_name = os.path.dirname(first_file)
        file_list = os.path.splitext(first_file)
        file_name = os.path.basename(file_list[0])

        for file in self.files:
            file_ext = os.path.splitext(file)[-1]
            if not os.path.exists(file):
                self.notify(f"{os.path.basename(file)}: does not exist.")
                continue
            if not self.check_if_pdf(file_ext):
                self.notify(f"{os.path.basename(file)}: is not a valid PDF file.")
                continue
            self.writer.append(file)

        if len(self.writer.pages) == 0:
            return
        nowtime = time.strftime("%Y-%m-%d_%H.%M.%S", time.localtime(time.time()))
        self.writer.write(f"{dir_name}\\{file_name}-merged-{nowtime}.pdf")
        self.writer.close()

    def split(self, input_file, file_name, output_dir):
        pdf = PdfReader(open(input_file, "rb"))
        for page_index in range(len(pdf.pages)):
            writer = PdfWriter()
            writer.add_page(pdf.pages[page_index])
            output_pdf_name = f"{output_dir}\\{file_name}-page-{page_index+1}.pdf"
            with open(output_pdf_name, 'wb') as output_file:
                writer.write(output_file)

    def split_execute(self):
        for file in self.files:
            file_list = os.path.splitext(file)
            dir_name = file_list[0]
            file_name = os.path.basename(file_list[0])
            file_ext = file_list[-1]
            if not os.path.exists(file):
                self.notify(f"{os.path.basename(file)}: does not exist.")
                continue
            if not self.check_if_pdf(file_ext):
                self.notify(f"{os.path.basename(file)}: is not a valid PDF file.")
                continue
            nowtime = time.strftime("%Y-%m-%d_%H.%M.%S", time.localtime(time.time()))
            output_dir = f"{dir_name}-splitted-{nowtime}"
            self.mkdir(output_dir)
            self.split(file, file_name, output_dir)


if __name__ == "__main__":
    op = sys.argv[1]
    files = sys.argv[2:]

    pdfiy = pdfiy(files)

    if len(files) == 0:
        pdfiy.notify("Please, select at least one  PDF file.")
        sys.exit(1)

    if op == "merge":
        pdfiy.merge()
    elif op == "split":
        pdfiy.split_execute()
    else:
        pdfiy.notify("Something went wrong.")
    sys.exit(1)