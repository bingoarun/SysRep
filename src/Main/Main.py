__author__ = 'Arun'
import time
from ExcelInput import *
import InformationManager
import ConnectionManager
import ExcelManager

#For finding total execution time
start_time = time.clock()

###############
storageconnection=None
exHand=None
excel=None
progress_count=None
total_system=None
attribute=None
##############

#######################################################################################################################
# 3PAR Information is hard coded for initial use
# Enter IP address and password for 3PAR Array. Although without these information other attributes can be obtained
# 3PAR IP Address
TPARIP='***********'
#3PAR Password
TPARPASS=['*******','********']


def createStorageConnection():
    tpar=Model(TPARIP,Category.TPAR,TPARPASS)
    storageconnection = ConnectionManager.createConnection(tpar)

    if storageconnection == None:
        print "Storage connection cannot be established."
    else:
        print "Storage connection established successfully."
    return storageconnection
#######################################################################################################################

#######################################################################################################################
# Inputs for execution
#INPUT_PATH="testinput.xlsx"
#OUTPUT_PATH=r"C:\Users\Arun\PycharmProjects\SysRep\Main\report.xlsx"

#######################################################################################################################


def showProgress(attribute):
    global progress_count,total_system
    print str( (round(((float(progress_count)*6.0)+float(attribute))/(6.0*float(total_system)),2))*100)+"% Completed"
    #print "progress count"+str(progress_count)+"attribute:"+str(attribute)



def loadAllvalues(sys):
  global progress_count
  progress_count=progress_count+1

  con= ConnectionManager.createConnection(sys)


  if con != None:
    print "Connection established to "+sys._primary_ip
    sys= InformationManager.getHostName(con,sys)
    print "Received hostname : "+sys._hostname
    showProgress(1)


    sys= InformationManager.getOSName(con,sys)
    print "Received OS details : " +ensure_str(sys._os)
    showProgress(2)

    sys= InformationManager.getModel(con,sys)
    print "Received Model : "+sys._type
    showProgress(3)

    sys= InformationManager.getIPAddr(con,sys)
    print "Received IP Address details : "+sys._ipaddr
    showProgress(4)

    sys= InformationManager.getMacAddr(con,sys)
    print "Received MAC address details : "+sys._macaddr
    showProgress(5)

    #sys=InformationManager.getWWN(con,sys)

    sys= InformationManager.getStorage(con,sys,storageconnection)
    print "Received Storage details : "+sys._wwn, sys._tparhost, sys._tparvolumes
    showProgress(6)

    #print sys._hostname
    ConnectionManager.closeConnection(con,sys)

    return sys
  else :
      sys._hostname =  "Error in "+sys._primary_ip
      return sys



#for sys in stand:
    #sys=Model #remove it #2min
def testth(sys,exHand,excel):
    sys=loadAllvalues(sys)
    ExcelManager.writeExcel(exHand,excel,sys)
    global progress_count
    print str(progress_count+1)+" of "+str(total_system) +" Completed\n"
    #progress_count=progress_count+1


#ExcelManager.generateSampleInput(r"c:/tmp/new.xlsx")

def Main(INPUT_PATH,OUTPUT_PATH):
    global storageconnection,exHand,excel,total_system,progress_count
    storageconnection=createStorageConnection()

    system=getSystemArray(INPUT_PATH)
    total_system=len(system)

    exHand,excel = ExcelManager.createConnection(OUTPUT_PATH)

    progress_count=-1

    print "Total number of systems:", total_system
    exHand,excel = ExcelManager.prepareSheet(exHand,excel)

    for sys in system:
        testth(sys,exHand,excel)
    closeAll()



def closeAll():
    global exHand
    try:
     ExcelManager.closeConnection(exHand)
     storageconnection.close()
    except:
        print "Some error occured in closing the application properly."
    print time.clock() - start_time, "seconds"

