from PyPDF2 import PdfWriter

import os

merge=PdfWriter()
files=[file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    merge.append(pdf)

merge.write("merged-pdf.pdf")
merge.close()