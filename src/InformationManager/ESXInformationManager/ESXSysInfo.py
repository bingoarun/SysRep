__author__ = 'Arun'

def getESXHostName(con):
    stdin, stdout, stderr = con.exec_command('hostname')
    return stdout.readlines()[0]

def getESXOS(con):
    stdin, stdout, stderr = con.exec_command('vmware -v')
    return stdout.readlines()[0]

def getESXModel(con):
    stdin, stdout, stderr = con.exec_command('esxcfg-info | grep \'Product Name\' | sed -n 1p')
    return stdout.readlines()[0].split('.')[-1]

