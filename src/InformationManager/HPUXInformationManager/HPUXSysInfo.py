__author__ = 'Arun'


def getHPUXHostName(con):
    stdin, stdout, stderr = con.exec_command('hostname')
    return stdout.readlines()[0]

def getHPUXOS(con):
   stdin, stdout, stderr = con.exec_command('swlist | grep DC')
   var= stdout.readlines()[0].split()
   return var[0]+" "+var[1]

def getHPUXModel(con):
    stdin, stdout, stderr = con.exec_command('model')
    return stdout.readlines()[0]