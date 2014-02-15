__author__ = 'Arun'
import xlrd
from Model import *

# To handle Unicode string problem
def ensure_str(s):
    if isinstance(s, unicode):
        s = s.encode('utf-8')
    return s

#Get array of systems from excel input file
def getSystemArray(input_path):
    workbook = xlrd.open_workbook(input_path)
    worksheet = workbook.sheet_by_index(0)

    num_rows=0
    for n in worksheet.col_values(0):
        if n !='':
            num_rows+=1
    num_rows-=1
    num_cells = worksheet.ncols - 1

    num_cells = 3
    curr_row = 0

    system=[]
    temp_sys=[]
    credentials=[]


    while curr_row < num_rows:
        curr_row+=1
        row = worksheet.row(curr_row)

        curr_cell = -1
        temp_sys=[]
        credentials =[]
        while curr_cell < num_cells:
            curr_cell+=1
            cell_value = worksheet.cell_value(curr_row,curr_cell)
            if curr_cell == 1:

                cell_value=int(cell_value)
            if curr_cell ==2:
                credentials.append(ensure_str(cell_value))
            if curr_cell ==3:
                credentials.append(ensure_str(cell_value))
            #print '' , cell_value,"# ",curr_cell
            temp_sys.append(cell_value)
        #print temp_sys[0],temp_sys[1],credentials
        system.append(Model(temp_sys[0],temp_sys[1],credentials))
    #print num_rows, num_cells
    return system