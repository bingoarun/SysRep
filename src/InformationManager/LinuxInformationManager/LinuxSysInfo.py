__author__ = 'Arun'


import paramiko

def getLinuxHostName(con):
    stdin, stdout, stderr = con.exec_command('hostname')
    return stdout.readlines()[0]

def getLinuxOS(con):
    stdin, stdout, stderr = con.exec_command('cat /etc/issue')
    return stdout.readlines()[0]

def getlinuxModel(con):
    stdin, stdout, stderr = con.exec_command('dmidecode | grep \'Product Name\'')
    str=''
    for i in stdout.readlines()[0].split()[2:]:
        str=str+" "+i
    return str



