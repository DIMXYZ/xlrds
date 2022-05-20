import os

from xlrd import *
filelocation = r"C:\Users\Administrateur\Downloads\LIST_VARIABLES_VEHICLES_COLLISION.xlsx"
wbk = xlrd.open_workbook(filelocation)
sheet = wbk.sheet_by_index(0)
print(sheet.cell_value(0,1))
