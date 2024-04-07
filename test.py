import os
# your_path = ' /home/username/Documents/Python/test.hello.pdf  '
# print(os.path.basename(your_path).split(".pdf")[0])

# print(len(your_path))
# print(len(your_path.strip()))

input_pdf = "C:/Users/ismail/dev/side-projects/pdf-merge-split/pdf-1.pdf"
input_pdf = input_pdf.strip()

input_pdf_splitted = os.path.splitext(input_pdf)

name = os.path.basename(input_pdf_splitted[0])
ext = input_pdf_splitted[-1]