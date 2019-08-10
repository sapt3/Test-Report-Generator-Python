from io import StringIO
import PyPDF2

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

packet = StringIO()

# create a new PDF with Reportlab
can = canvas.Canvas("mypdf.pdf", pagesize=letter)
can.drawString(100, 100, "Hello world")
can.save()

# move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PyPDF2.PdfFileReader(packet)
# read your existing PDF

existing_pdf = PyPDF2.PdfFileReader(open("mypdf.pdf", "r"))

output = PyPDF2.PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = open("/home/joe/newpdf.pdf", "w")
output.write(outputStream)
outputStream.close()
