from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open("C:/Users/teo/Downloads/Telegram Desktop/Computer Organization and Design 5.pdf","rb"))


a = int(input()) + 22
b = int(input()) + 23

output = PdfFileWriter()

for i in range(a,b):
	
	output.addPage(inputpdf.getPage(i))


with open("semana 2.pdf", "wb") as outputStream:
	output.write(outputStream)