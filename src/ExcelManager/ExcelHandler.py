__author__ = 'Arun'
import ExcelConnection
import xlsxwriter
# Counter set to 2 to ignore the heading in first line of excel file
counter=2

# Initialize the Excel sheet by creating titles and set text wrap
def prepareSheet(workbook,worksheet):
    bold = workbook.add_format({'bold': 1})
    wrap = workbook.add_format()
    wrap.set_text_wrap()
    workbook.add_format({})
    worksheet.set_column('A:A', 20)
    worksheet.set_column('B:B', 20)
    worksheet.set_column('C:C', 30)
    worksheet.set_column('D:D', 50)
    worksheet.set_column('E:E', 30)
    worksheet.set_column('F:F', 30)
    worksheet.set_column('G:G', 30)
    worksheet.set_column('H:H', 30)
    worksheet.set_column('I:I', 30)
    worksheet.set_column('J:J', 30)
    return workbook,worksheet


def writeExcel(workbook,worksheet,sys):
    #sys=Model
    global counter


    wrap = workbook.add_format()
    wrap.set_text_wrap()

    worksheet.write('A'+str(counter), sys._hostname)
    #print 'A'+str(counter), sys._hostname
    worksheet.write('B'+str(counter), sys._passcat[0]+"\n"+sys._passcat[1],wrap)
    worksheet.write('C'+str(counter), sys._type,wrap)
    worksheet.write('D'+str(counter), sys._os,wrap)
    worksheet.write('E'+str(counter), sys._ipaddr,wrap)
    worksheet.write('F'+str(counter), sys._macaddr,wrap)
    worksheet.write('G'+str(counter), sys._tparhost,wrap)
    worksheet.write('H'+str(counter), sys._tparvolumes,wrap)
    worksheet.write('I'+str(counter), sys._wwn,wrap)
    worksheet.write('J'+str(counter), sys._lun,wrap)

    counter=counter+1


# Function to generate sample input template excel file
def generateSampleInput(path):

    workbook = xlsxwriter.Workbook(path)
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': 1})

    worksheet.write('A1',"IP Addesss",bold)
    worksheet.write('B1',"Category",bold)
    worksheet.write('C1',"Username",bold)
    worksheet.write('D1',"Password",bold)

    worksheet.write('F1',"Category list",bold)
    worksheet.write('F2',"TYPE",bold);worksheet.write('G2',"ID",bold)
    worksheet.write('F3',"Windows");worksheet.write('G3',"1")
    worksheet.write('F4',"Linux");worksheet.write('G4',"2")
    worksheet.write('F5',"HPUX");worksheet.write('G5',"3")
    worksheet.write('F6',"ESX");worksheet.write('G6',"4")

    workbook.close()

