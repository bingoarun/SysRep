__author__ = 'Arun'
import xlsxwriter

def createConnection(PATH):
    workbook = xlsxwriter.Workbook(PATH)
    worksheet = workbook.add_worksheet()
    return workbook,worksheet

def closeConnection(workbook):
    workbook.close()


