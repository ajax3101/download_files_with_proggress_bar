from pdf2docx import Converter

pdf_file = 'sobes.pdf'
docx_file = 'sobes.docx'

# convert pdf to docx
cv = Converter(pdf_file)

# all pages by default
cv.convert(docx_file)
cv.close()