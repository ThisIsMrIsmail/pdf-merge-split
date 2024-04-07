from pypdf import PdfWriter
import time

merger = PdfWriter()

for pdf in ["pdf-1.pdf", "pdf-2.pdf"]:
    merger.append(pdf)

nowtime = time.strftime("%Y-%m-%d_%H.%M.%S", time.localtime(time.time()))
merger.write(f"merged-pdf-{nowtime}.pdf")
merger.close()