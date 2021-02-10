"""
Onderstaande is de template of een proof-of-work voor het aanpassen van properties van pdf documenten (pdf).
het is niet mogelijk om in-place veranderingen te automatiseren. daarom wordt de gehele inhoud van het document
gekopieerd naar een nieuw document.
ook de properties van het oude document worden overgenomen. daarbij kunnen de properties van het nieuwe document
aangepast of toegevoegd worden voordat het nieuwe document wordt opgeslagen.
tot slot wordt het orginele document verwijderd en krijgt het nieuwe document de naam van het orginele (verwijderde)
document.

source:
http://kitchingroup.cheme.cmu.edu/blog/2013/06/13/Reading-and-writing-pdf-metadata/
"""
# todo: deze aanpak moet nog verder getest worden (verdere uitleg hieronder)
"""
Wanneer dit proces meerdere keren wordt uitgevoerd, wordt er een error gegenereerd. Probeer het proces vijf keer achter
elkaar uit te voeren met elke keer andere waarden voor de te veranderen properties
 title=None, subject=None, keywords=None, category=None, comments=None
 
 ZIE AANTEKENINGEN OP A4
"""
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import NameObject, createStringObject
import os

# Naam van het orginele document (en uiteindelijk ook voor het nbieuwe document
name = 'Continental White Cap.pdf'

# defniëren van de paden/namen van de in- en output documenten
file_name = f'doc\\{name}'
output_file = f'doc\\test-{name}'

# openen van het orginele bestand
file = open(file_name, 'rb')
pdf_in = PdfFileReader(file)

# ophalen van de properties van het orginele document (is niet van belang voor de werking van het script)
props = pdf_in.documentInfo

# Definiëren van de writer
writer = PdfFileWriter()

# overschrijven van de pagina's (inhoud) naar de writer
print(range(pdf_in.getNumPages()))
for page in range(pdf_in.getNumPages()):
    writer.addPage(pdf_in.getPage(page))

# Verwijzen naar beschermde member van de writer class (_info) infoDict ook wel propertyDict o.i.d.
infoDict = writer._info.getObject()

# overschrijven van de properties van het oude document naar de writer
for key in props:
    infoDict.update({NameObject(key): createStringObject(props[key])})

# toewijzen van een titel in de properties
title = 'titletest'
keywords = None

None if title is None else infoDict.update({NameObject('/Title'): createStringObject(title)})
None if keywords is None else infoDict.update({NameObject('/Keywords'): createStringObject(keywords)})

# infoDict.update({NameObject('/Title'): createStringObject('testtest')})
# infoDict.update({NameObject('/Subject'): createStringObject('subtest')})
# infoDict.update({NameObject('/Keywords'): createStringObject('keytest')})
# infoDict.update({NameObject('/Category'): createStringObject('categorytest')})
# infoDict.update({NameObject('/Comments'): createStringObject('Commentstest')})

# output file openen
pdf_out = open(output_file, 'wb')

# alles schrijven naar output file
writer.write(pdf_out)

# sluiten van het oude en nieuwe bestand
file.close()
pdf_out.close()

# Verwijderen van het oorspronkelijk document en het hernoemen van het nieuwe document
# Zo lijkt het alsof er niets gebeurd is
os.unlink(file_name)
os.rename(output_file, file_name)
