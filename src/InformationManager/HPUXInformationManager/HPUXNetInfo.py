__author__ = 'Arun'

def getHPUXIPName(con):
    stdin, stdout, stderr = con.exec_command(r"cat /etc/rc.config.d/netconf | grep -F INTERFACE_NAME[")
    ipname= ""
    for i in stdout.readlines():
        ipname = ipname + i.split('\"', 1)[1].split('\"')[0] + "\n"
    return ipname


def getHPUXIPAddr(con):
    stdin, stdout, stderr = con.exec_command(r"cat /etc/rc.config.d/netconf | grep -F IP_ADDRESS[")
    ip= ''
    for i in stdout.readlines():
        if '\"' in i:
         ip = ip + i.split('\"', 1)[1].split('\"')[0] + "\n"
        else:
         ip= ip + i.split('=')[1].rstrip() +"\n"
    return ip

def getHPUXMACAddr(con):
    stdin, stdout, stderr = con.exec_command(r"cat /etc/rc.config.d/netconf | grep -F INTERFACE_NAME[")
    ip= ''
    mac=''
    for i in stdout.readlines():
        #ip = ip + i.split('\"', 1)[1].split('\"')[0] + "\n"


        stdin1, stdout1, stderr1 = con.exec_command(r"lanscan")
        ip= ''
        for j in stdout1.readlines():
            if '\"' in i:            # "lan0" format
                if  j.split()[4] == i.split('\"', 1)[1].split('\"')[0]:
                    mac=mac+j.split()[1][2:]+"\n"
            else:                    # lan0 format
                if  j.split()[4] == i.split("=")[1].rstrip():
                    mac=mac+j.split()[1][2:]+"\n"

    return mac