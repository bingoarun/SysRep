__author__ = 'Arun'
#esxcfg-nics -l

def getESXIPAddr(con):
    stdin, stdout, stderr = con.exec_command('hostname -i')
    return stdout.readlines()[0]


def getESXMACAddr(con):
    stdin, stdout, stderr = con.exec_command('esxcfg-nics -l | tail +2')
    # $0 for name
    temp1=stdout.readlines()

    strmac=''

    for i in temp1:
        strmac=strmac+i.split()[6]+"\n"
        #temp1[j]=temp1[j]+stdout.readlines()[0]


    return strmac