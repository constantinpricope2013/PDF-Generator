# Content
file_name = 'result.pdf'
document_title = 'Titlu documentului!'
title = 'Titlu per pagina.'
subtitle = 'Subtitlu'

from reportlab.pdfgen import canvas

pdf = canvas.Canvas(file_name)
#set title
pdf.setTitle(document_title)
#write in pdf
pdf.drawString(0, 0, title)



pdf.save()