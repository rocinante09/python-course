import PyPDF2
import sys


def rotatePDF():        # lesson 218
    with open('dummy.pdf', 'rb') as my_file:
        reader = PyPDF2.PdfFileReader(my_file)
        page = reader.getPage(0)
        print(page.rotateCounterClockwise(90))
        writer = PyPDF2.PdfFileWriter()
        writer.addPage(page)
        with open('tilt.pdf', 'wb') as file:
            writer.write(file)


def mergePDF(pdfs):        # lesson 219
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdfs:
        print(pdf)
        merger.append(pdf)
    merger.write('merged_pdf.pdf')

def pwd_watermark(source_file, watermark_file, target_file):

    reader = PyPDF2.PdfFileReader(watermark_file)
    watermark = reader.pages[0]

    writer = PyPDF2.PdfFileWriter()

    reader = PyPDF2.PdfFileReader(source_file)
    pages = list(range(0, len(reader.pages)))
    for index in pages:
        content_page = reader.pages[index]
#        mediabox = content_page.mediaBox
        content_page.mergePage(watermark)
#        content_page.mediaBox = mediabox
        writer.addPage(content_page)

    with open(target_file, "wb") as fp:
        writer.write(fp)



#inputs = sys.argv[1:]
#mergePDF(inputs)

inputs = sys.argv[1:]
print(inputs)
pwd_watermark(inputs[0], inputs[1], inputs[2])