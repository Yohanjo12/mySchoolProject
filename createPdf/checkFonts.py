from reportlab.pdfgen import canvas

pdf = canvas.Canvas("Filename.pdf")

for font in pdf.getAvailableFonts():
	print(font)