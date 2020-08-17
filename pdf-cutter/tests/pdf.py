#!/usr/bin/env python

from sys import argv
import os.path
from PyPDF4 import PdfFileWriter, PdfFileReader
from typing import List

import math 
import typer


def main(input_name: str, pages: List[str], output_name: str):
	input_pdf = PdfFileReader(open(input_name,"rb"))
	output = PdfFileWriter()

	if os.path.isfile('./' + output_name):
		ow = typer.confirm("This file already exists, want to overwrite it?")
		if not ow:
			raise typer.Abort()
	
	if not output_name.endswith('.pdf'):
		typer.echo("Make sure the last argument is the output file. It should end with '.pdf'.")
		raise typer.Exit()


	for i in pages:
		print(i)
		if '-' in i:
			initial, final = (int(x) for x in i.split('-'))
			for j in range(initial, final):
				output.addPage(input_pdf.getPage(j))
				
		else:
			output.addPage(input_pdf.getPage(int(i)))
	
	with open("{}".format(output_name), "wb") as outputStream:
				output.write(outputStream)	


if __name__ == "__main__":
	typer.run(main)