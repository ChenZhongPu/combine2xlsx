__version__ = '0.1.9'
import xlrd
import xlsxwriter

def combine(input_list, output='output.xlsx'):
	output_work = xlsxwriter.Workbook(output)
	result_sheet = output_work.add_worksheet()
	input_sheet_list = []
	for i in input_list:
		input_sheet_list.append(xlrd.open_workbook(i).sheet_by_index(0))

	columns = input_sheet_list[0].ncols
	first_rows = input_sheet_list[0].nrows

	for row_id in range(0, first_rows):
		for column_id in range(0, columns):
			result_sheet.write(row_id, column_id, input_sheet_list[0].cell(rowx=row_id, colx=column_id).value)
	row_to_write = first_rows
	for index, sheet in enumerate(input_sheet_list):
		if index > 0:
			for row_id in range(1, sheet.nrows):
				for column_id in range(0, columns):
					result_sheet.write(row_to_write + row_id - 1, column_id, sheet.cell(rowx=row_id, colx=column_id).value)
			row_to_write += sheet.nrows - 1

	output_work.close()