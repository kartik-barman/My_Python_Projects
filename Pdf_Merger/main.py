from PyPDF2 import PdfMerger

all_pdf = ["my.pdf", "my2.pdf"]

merger = PdfMerger()

for newPdf in all_pdf:
    merger.append(newPdf)


merger.write("kartik.pdf")