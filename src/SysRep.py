__author__ = 'Arun'
import sys, getopt
import ExcelManager

ifile=''
ofile=''

def print_help():
        print "\nTo generate a sample input Excel file:\n\n\t SysRep --sample <PATH_FOR_GENERATING_SAMPLE>\n\n"
        print "To generate report from input file:\n\n\t SysRep -i <INPUT_EXCEL_FILE_PATH> -o <OUTPUT_EXCEL_FILE_PATH>\n"

if len(sys.argv)==2 and sys.argv[1]=='--help':
        print_help()

elif len (sys.argv)==5 and (sys.argv[1]=='-i' or sys.argv[1]=='-o') and (sys.argv[3]=='-i' or sys.argv[3]=='-o'):

 try:
    myopts, args = getopt.getopt(sys.argv[1:],"i:o:")
 except getopt.GetoptError as e:
    print (str(e))
    print("Usage: %s -i input -o output" % sys.argv[0])
    sys.exit(2)

 for o, a in myopts:
    if o == '-i':
        ifile=a
    elif o == '-o':
        ofile=a


 # Display input and output file name passed as the args
 print ("Input file : %s and output file: %s" % (ifile,ofile) )
 global INPUT_PATH, OUTPUT_PATH
 INPUT_PATH=str(ifile)
 OUTPUT_PATH=str(ofile)
 from Main import Main
 Main(INPUT_PATH,OUTPUT_PATH)

elif len(sys.argv)==3 and sys.argv[1]=='--sample':
        ExcelManager.generateSampleInput(str(sys.argv[2]))
        print "Sample input template is saved in :"+str(sys.argv[2])
else:
        print "Invalid number or usage of arguments\n\n Enter 'SysRep --help' for help"

