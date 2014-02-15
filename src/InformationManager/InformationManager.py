__author__ = 'Arun'
from Model import *

from WindowsInformationManager import *
from LinuxInformationManager import *
from TPARInformationManager import *
from HPUXInformationManager import *
from ESXInformationManager import *


#sys=Model

def getHostName(con, sys):
    #sys=Model
  try:
    if sys._category == Category.WIN:
        sys._hostname = getWinHostName(con)

    elif sys._category == Category.LINUX:
        sys._hostname = getLinuxHostName(con)

    elif sys._category == Category.HPUX:
        sys._hostname = getHPUXHostName(con)

    elif sys._category == Category.ESX:
        sys._hostname = getESXHostName(con)
    return sys
  except:
      print "Error in retrieving Hostname for ",sys._primary_ip
      sys._hostname = "ERROR"
      return sys




def getOSName(con, sys):
    #sys=Model
  try:
    if sys._category == Category.WIN:
        sys._os = getWinOS(con)

    elif sys._category == Category.LINUX:
        sys._os = getLinuxOS(con)

    elif sys._category == Category.HPUX:
        sys._os = getHPUXOS(con)

    elif sys._category == Category.ESX:
        sys._os = getESXOS(con)
    return sys
  except:
      print "Error in retrieving OS information for ",sys._primary_ip
      sys._os = "ERROR"
      return sys


def getModel(con, sys):
    #sys=Model
  try:
    if sys._category == Category.WIN:
        sys._type = getWinModel(con)

    elif sys._category == Category.LINUX:
        sys._type = getlinuxModel(con)

    elif sys._category == Category.HPUX:
        sys._type = getHPUXModel(con)

    elif sys._category == Category.ESX:
        sys._type = getESXModel(con)

    return sys
  except:
      print "Error in retrieving Model for ",sys._primary_ip
      sys._type = "ERROR"
      return sys


def getMacAddr(con, sys):
    #sys=Model
  try:
    if sys._category == Category.WIN:
        sys._macaddr = getWinMacAddr(con)

    elif sys._category == Category.LINUX:
        sys._macaddr = getLinuxMACAddr(con)

    elif sys._category == Category.HPUX:
        sys._macaddr = getHPUXMACAddr(con)

    elif sys._category == Category.ESX:
        sys._macaddr = getESXMACAddr(con)

    return sys
  except:
      print "Error in retrieving MAC Address for ",sys._primary_ip
      sys._macaddr = "ERROR"
      return sys


def getIPAddr(con, sys):
    #sys=Model
  try:
    if sys._category == Category.WIN:
        sys._ipaddr = getWinIPAddr(con)

    elif sys._category == Category.LINUX:
        sys._ipaddr = getLinuxIPAddr(con)

    elif sys._category == Category.HPUX:
        sys._ipaddr = getHPUXIPAddr(con)

    elif sys._category == Category.ESX:
        sys._ipaddr = getESXIPAddr(con)

    return sys
  except:
      print "Error in retrieving IP for ",sys._primary_ip
      sys._ipaddr = "ERROR"
      return sys


def getStorage(con, sys, storageconnection):
    #sys=Model
  try:
    tempwwn = ''
    if sys._category == Category.WIN:
        tempwwn = getWinWWN(con)
        # Need to change this code once figured out a way to find Windows WWN
        tempwwn = '5001438009AE831A'

    elif sys._category == Category.LINUX:
        tempwwn = getLinuxWWN(con)

    elif sys._category == Category.HPUX:
        tempwwn = getHPUXWWN(con, storageconnection)

    elif sys._category == Category.ESX:
        tempwwn = getESXWWN(con, storageconnection)

    sys._tparhost, sys._tparvolumes, sys._wwn, sys._lun = getStorageInformation(storageconnection, tempwwn)

    sys._tparhost=sys._tparhost.split('\n')
    sys._tparhost= " ".join(sorted(set(sys._tparhost), key=sys._tparhost.index))

    sys._tparvolumes=sys._tparvolumes.split('\n')
    sys._tparvolumes= " ".join(sorted(set(sys._tparvolumes), key=sys._tparvolumes.index))

    sys._wwn=sys._wwn.split('\n')
    sys._wwn= " ".join(sorted(set(sys._wwn), key=sys._wwn.index))

    return sys
  except:
      print "Error in retrieving WWN for ",sys._primary_ip
      sys._tparhost = "ERROR"
      sys._tparvolumes = "ERROR"
      sys._wwn = "ERROR"
      return sys


