"""
Onderstaande is de template of een proof-of-work voor het aanpassen van properties van word documenten (docx).

source:
https://python-docx.readthedocs.io/en/latest/dev/analysis/features/coreprops.html
"""
from docx import Document

docx_file = 'doc\\Differentiërende factoren.docx'

document = Document(docx_file)

props = document.core_properties

print(props)
props.title = 'test'

# Belangrijk bij deze aanpak is dat het na de veranderingen ook nog wordt opgeslagen
document.save(docx_file)
