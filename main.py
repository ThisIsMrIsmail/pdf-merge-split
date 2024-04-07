from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["pdf-1.pdf", "pdf-2.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()