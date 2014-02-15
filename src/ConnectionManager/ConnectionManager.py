__author__ = 'Arun'
from WindowsConnectionManager import *
from UnixConnectionManager import *
from Model import *


def createConnection(sys):
   #sys=Model
  try:
   con=None
   if sys._category==Category.WIN:
       con=createWinConnection(sys)
   elif sys._category==Category.LINUX:
       con=createUnixConnection(sys)
   elif sys._category==Category.HPUX:
       con=createUnixConnection(sys)
   elif sys._category==Category.ESX:
       con=createUnixConnection(sys)
   elif sys._category==Category.TPAR:
       con=createUnixConnection(sys)
   return con
  except:
      print "Error in establishing connection to " , sys._primary_ip
      return None


def closeConnection(con,sys):
  try:
    if sys._category==Category.WIN:
       con=None
    elif sys._category==Category.LINUX:
       endUnixConnection(con)
    elif sys._category==Category.HPUX:
       endUnixConnection(con)
    elif sys._category==Category.ESX:
       endUnixConnection(con)
    return con
  except:
      print "Error in closing connection:",sys._primary_ip
      return None

