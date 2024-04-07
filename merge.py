from pypdf import PdfWriter
import time

writer = PdfWriter()

for pdf in ["pdf-1.pdf", "pdf-2.pdf"]:
    writer.append(pdf)

nowtime = time.strftime("%Y-%m-%d_%H.%M.%S", time.localtime(time.time()))
writer.write(f"merged-pdf-{nowtime}.pdf")
writer.close()