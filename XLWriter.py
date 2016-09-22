from xlrd import open_workbook
from openpyxl import load_workbook
import csv


filestring = "produse_ordonate.xlsx"

### Open source workbook ###

workbook = open_workbook(filestring)
sheet = workbook.sheet_by_index(0)

### Read data from source column ###

# Initialise empty lists which will store values
data1 = []

def readsource(sheet,lst, column):
	distinct = []
	same = []
	j = 0
	for i in range(sheet.nrows):
		llstbal = sheet.cell_value(i-1,column).lower()
		lstval = sheet.cell_value(i, column).lower()
		if (llstbal == lstval):
			j = j+1
			same += [lstval]
		else:
			distinct += [lstval]
	distinct = distinct[1:]
	print j
	return distinct, same


[distinct, same] = readsource(sheet, data1, 2)




