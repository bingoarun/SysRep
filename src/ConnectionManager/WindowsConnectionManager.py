__author__ = 'Arun'

import wmi
import pythoncom

def createWinConnection(sys):
    #sys=Model # remove it
    pythoncom.CoInitialize ()
    con = wmi.WMI(sys._primary_ip, user=sys._passcat[0], password=sys._passcat[1])
    #
    #print sys._primary_ip, sys._passcat[0], sys._passcat[1]
    return con

def endWinConnection():
    #test
    return None





