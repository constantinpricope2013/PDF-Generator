# ###################################
# Help
def drawMyRuler(pdf):
    print("Inside drawMyRuler")
    pdf.drawString(100,810, 'x100')
    pdf.drawString(200,810, 'x200')
    pdf.drawString(300,810, 'x300')
    pdf.drawString(400,810, 'x400')
    pdf.drawString(500,810, 'x500')

    pdf.drawString(10,100, 'y100')
    pdf.drawString(10,200, 'y200')
    pdf.drawString(10,300, 'y300')
    pdf.drawString(10,400, 'y400')
    pdf.drawString(10,500, 'y500')
    pdf.drawString(10,600, 'y600')
    pdf.drawString(10,700, 'y700')
    pdf.drawString(10,800, 'y800')  



# Content
print("Setting content")
file_name = 'result.pdf'
document_title = 'Titlu documentului!'
title = 'Titlu per pagina.  Final'
subtitle = 'Subtitlu'

print("Preparing importing")
from reportlab.pdfgen import canvas

pdf = canvas.Canvas(file_name)
#set title
pdf.setTitle(document_title)
#write in pdf
#pointers:
drawMyRuler(pdf)
pdf.drawString(200, 200, title)


print("Saving pdf..")
pdf.save()