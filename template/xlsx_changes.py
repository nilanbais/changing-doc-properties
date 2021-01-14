"""
Onderstaande is de template of een proof-of-work voor het aanpassen van properties van excel documenten (xlsx).

!!!LET OP!!!
openpyxl does currently not read all possible items in an Excel file so images and charts will be lost from existing
files if they are opened and saved with the same name.

Bovenstaande komt uit de openpyxl documentatie
(https://openpyxl.readthedocs.io/en/stable/usage.html#read-an-existing-workbook)

source:
https://stackoverflow.com/questions/52120125/how-to-edit-core-properties-of-xlsx-file-with-python
"""
import openpyxl

name = 'Calculatie Exploitatie Rijnlandroute versie 0.14.xlsx'
input_filename = f'doc\\{name}'
output_filename = f'doc\\test-{name}'

input_file = openpyxl.load_workbook(input_filename)

print(input_file.sheetnames)

props = input_file.properties

props.title = 'testtest'

input_file.save(input_filename)

"""
De aanpak waarin de gehele inhoud wordt gekoieerd naar een nieuw document met de aangepaste properties werkt niet
zoals gewenst, door dat de opmaak van het document niet wordt overgenomen. Kijk naar de mogelijkheid om de 
properties van een document aan te passen om het vervolgens op te slaan.
"""
