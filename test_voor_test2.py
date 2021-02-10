from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import NameObject, createStringObject
import os

# Naam van het orginele document (en uiteindelijk ook voor het nbieuwe document
name = 'Continental White Cap.pdf'

# defniëren van de paden/namen van de in- en output documenten
file_name = f'doc\\{name}'

# openen van het orginele bestand
file = open(file_name, 'rb')
pdf_in = PdfFileReader(file)

props = pdf_in.documentInfo

