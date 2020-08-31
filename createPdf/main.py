from reportlab.pdfgen import canvas

dataSiswa = {
	"nama" : "Decade",
	"kelas" : "-",
	"laporan" : "Rapot"
}

class Data:

	def __init__(self, filename, documentTitle, heading):
		self.filename = filename
		self.documentTitle = documentTitle
		self.heading = heading
		self.info = "Decade 9.2"


myData = Data(str(dataSiswa['nama']+dataSiswa['kelas']+".pdf"), "Hasil Ujian", dataSiswa['laporan'])
myPdf = canvas.Canvas(myData.filename)
myPdf.setTitle(myData.documentTitle)

#myPdf.drawString(285,800,myData.heading)#x,y

myPdf.setFont("Helvetica", 40)
myPdf.setFillColorRGB(30,0,0)
myPdf.drawCentredString(300, 770,"LAPORAN")
myPdf.line(30, 760, 580, 760)


myText = myPdf.beginText(40,680)
myText.setFont("Helvetica", 14)

Lines = ["Kamen Rider Decade", "Decade, adalah Kamen Rider Heisei kesepuluh.","Slogan dari seri ini adalah Hancurkan Semua.", "Hubungkan Semua! Yang menarik dalam serial ini adalah karena Decade memiliki ","kekuatan untuk mengubah wujudnya menjadi kamen rider heisei terdahulunya."]
for line in Lines:
	myText.textLine(line)

myPdf.drawText(myText)

myPdf.drawInlineImage("decade.JPG", 200,0)

myPdf.save()
#print("OK")
