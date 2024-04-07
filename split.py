from pypdf import PdfReader, PdfWriter

input_pdf = PdfReader(open("1.pdf", "rb"))

writer = PdfWriter()

for page_num in range(len(input_pdf.pages)):
    writer.add_page(input_pdf.pages[page_num])

file_name = 'file_name.pdf'

with open(file_name, 'wb') as output_pdf:
    writer.write(output_pdf)