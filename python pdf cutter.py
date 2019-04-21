from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open("C:/Users/teo/Downloads/Telegram Desktop/Computer Organization and Design 5.pdf","rb"))

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
		print (len(entrada))
		if (len(entrada) > 1):
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
