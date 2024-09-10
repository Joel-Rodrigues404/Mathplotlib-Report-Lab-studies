from reportlab.pdfgen import canvas
from reportlab.lib.units import inch


def hello(c: canvas.Canvas):

    textobject = c.beginText(100, 100)
    c.drawText(textobject)

    # move the origin up and to the left
    c.translate(inch, inch)
    # define a large font
    c.setFont("Helvetica", 14)
    # choose some colors
    c.setStrokeColorRGB(0.2, 0.5, 0.3)
    c.setFillColorRGB(1, 0, 1)
    # draw some lines
    LINES = [(0, 0, 0, 1.7 * inch), (0, 0, 1 * inch, 0)]

    c.grid([50, 100, 150, 200], [50, 100, 150, 200])

    c.bezier(50, 10, 100, 60, 150, 85, 200, 90)

    c.arc(300, 400, 500, 600)

    c.rect(200, 200, 100, 50, stroke=1, fill=0)

    c.ellipse(350, 200, 400, 250, stroke=1, fill=0)

    c.wedge(200, 500, 250, 600, startAng=10, extent=50, stroke=1, fill=0)

    c.circle(250, 500, 100, stroke=1, fill=0)

    c.roundRect(300, 100, 50, 100, 10, stroke=1, fill=0)

    c.lines(LINES)
    # draw a rectangle
    c.rect(0.2 * inch, 0.2 * inch, 1 * inch, 1.5 * inch, fill=1)
    # make text go straight up
    c.rotate(90)
    # change color
    c.setFillColorRGB(0, 0, 0.77)
    # say hello (note after rotate the y coord needs to be negative!)
    c.drawString(0.3 * inch, -inch, "Hello World")
    c.drawRightString(0, 0, 'drawRightString')
    c.drawCentredString(10, 10, 'drawCentredString')

    path = c.beginPath()
    c.drawPath(path, stroke=1, fill=0, fillMode=None)
    c.clipPath(path, stroke=1, fill=0, fillMode=None)


cv = canvas.Canvas("pdfs/drawing_operations.pdf")

hello(cv)

cv.showPage()
cv.save()
