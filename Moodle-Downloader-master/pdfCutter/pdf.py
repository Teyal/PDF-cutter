from PyPDF2 import PdfFileWriter, PdfFileReader

#inputpdf = PdfFileReader(open("C:/Users/teo/Downloads/Telegram Desktop/Computer Organization and Design 5.pdf","rb"))
inputpdf = PdfFileReader(open("book/Computer Organization and Design 5.pdf","rb"))

output = PdfFileWriter()

number = 0.0

while True:
	try:
		entr = input()
		if (entr == ''):
				break
		if ('.' in entr):
			number = entr
			break
		entrada = entr.split()
		#could print somehting to make it better
		if (len(entrada) > 1):
			if 'A' in entr:
				primeira = int(entrada[0][1:]) + 574 + 22 #574 is the page where the A-xx start
				ultima = int(entrada[1][1:]) + 574 + 23
			else:
				primeira = int(entrada[0]) + 22
				ultima   = int(entrada[1]) + 23

			for i in range(primeira, ultima):
				output.addPage(inputpdf.getPage(i))
		else:
			pagina = int(entrada[0]) + 22
			output.addPage(inputpdf.getPage(pagina))
	except EOFError:
		break


with open("semana {}.pdf".format(entr), "wb") as outputStream:
	output.write(outputStream)
