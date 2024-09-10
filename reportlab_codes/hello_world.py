from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4

print(A4)

c = canvas.Canvas("pdfs/hello.pdf", pagesize=A4, verbosity=1)
c.drawString(9 * cm, 22 * cm, "Hello World!")
c.showPage()
c.save()
