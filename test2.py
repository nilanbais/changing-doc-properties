import xlsxwriter

name = 'Beoordelingsformulier Nilan Bais 2020 - kopie.xlsx'
input_filename = f'doc\\{name}'
output_filename = f'doc\\test-{name}'

workbook = xlsxwriter.Workbook(input_filename, {'in_memory': True})

# worksheet = workbook.get_worksheet_by_name()
print(workbook.sheetnames)

# for sheet in workbook.sheetnames:
#

workbook.set_properties({
    'title': 'test',
    'subject': 'testtest'
})

workbook.close()
