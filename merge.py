from pypdf import PdfWriter
import time
import sys
import os

writer = PdfWriter()

files = sys.argv[1:]
    
if len(files) == 0:
    print("Please provide a PDF file.")
    sys.exit(1)

for file in files:
    if not os.path.exists(file):
        print(f"File does not exist: {file}")
        time.sleep(3)
        sys.exit(1)
    writer.append(file)

nowtime = time.strftime("%Y-%m-%d_%H.%M.%S", time.localtime(time.time()))
writer.write(f"merged-pdf-{nowtime}.pdf")
writer.close()