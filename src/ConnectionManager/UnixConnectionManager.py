__author__ = 'Arun'

import paramiko

def createUnixConnection(sys):
    #sys=Model
    con = paramiko.SSHClient()
    con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    con.connect(sys._primary_ip, username=sys._passcat[0], password=sys._passcat[1])
    return con

def endUnixConnection(con):
    #test
    con.close()
    return None

