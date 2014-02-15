__author__ = 'Arun'

def getLinuxIPAddr(con):
    stdin, stdout, stderr = con.exec_command('ifconfig | grep \'Link encap\' | awk {\'print $1 , $5\'}')
    temp1=stdout.readlines()
    j=0
    strIP=''
    for i in temp1:
        str='ifconfig '+i.split()[0]+' | grep \'inet addr\'| awk {\'print $2\'}'
        stdin, stdout, stderr = con.exec_command(str)
        var=stdout.readlines()[0]
        if var[0:2]!='lo':
         strIP=strIP+var[5:]

        j=j+1
    return strIP


def getLinuxMACAddr(con):
    stdin, stdout, stderr = con.exec_command('ifconfig | grep \'Link encap\' | awk {\'print $5\'}')
    # $1 for name
    temp1=stdout.readlines()

    strmac=''

    for i in temp1:
        strmac=strmac+i

    return strmac


