import openpyxl

name = 'Calculatie Exploitatie Rijnlandroute versie 0.14.xlsx'
input_filename = f'doc\\{name}'
output_filename = f'doc\\test-{name}'

input_file = openpyxl.load_workbook(input_filename)

print(input_file.sheetnames)

props = input_file.properties

props.title = 'testtest'
props.keywords = 'keytest a mattie'

input_file.save(input_filename)
