__author__ = 'Arun'
import paramiko


#Function to check if WWN is present in the storageconnection provided
def checkWWNPresent (wwn,storageconnection):
    stdin, stdout, stderr = storageconnection.exec_command('showvlun')
    lis=stdout.readlines()
    twwn=''
    for i in lis[2:]:
       #print i.split()[3]
      try:
        #to ignore all unfilled data in the end
        if len(i.split()) >= 6:
         if i.split()[3]==wwn:
            twwn=wwn
      except IndexError:
        print 'Error'
    if twwn == '':
        return 1
    else:
        return 0


#Can't figure out a way to get Windows WWN, working on it
def getWinWWN(con):
    tempwwn=None
    return tempwwn

def getLinuxWWN(con):
    stdin, stdout, stderr = con.exec_command('sed -n 1p /sys/class/scsi_host/host1/device/fc_host:host1/port_name')
    return stdout.readlines()[0][2:18].upper()

def getHPUXWWN(con,storageconnection):
    stdin, stdout, stderr = con.exec_command(r"for i in `ioscan -kfnC fc | grep /dev | awk '{print $1}'`; do /opt/fcms/bin/fcmsutil $i | grep -w 'Driver state = ONLINE' > /dev/null 2>&1; if [ `echo $?` -eq '0' ]; then /opt/fcms/bin/fcmsutil $i | grep -w 'N_Port Port World Wide Name' | awk -F '=' '{print $2}' | awk -F 'x' '{print $2}';  fi; done")
    wwn=''
    for i in stdout.readlines():
        tmp=i.rstrip().upper()
        if checkWWNPresent(tmp,storageconnection) == 0:
            wwn=tmp
    return wwn

def getESXWWN(con,storageconnection):
    #esxcfg-scsidevs -a | grep fc | awk {'print $4'} | cut -c 21-36
    stdin, stdout, stderr = con.exec_command(r"esxcfg-scsidevs -a | grep fc | awk {'print $4'} | cut -c 21-36")
    wwn=''
    for i in stdout.readlines():
        tmp=i.rstrip().upper()
        if checkWWNPresent(tmp,storageconnection) == 0:
            wwn=tmp
    return wwn


def getStorageInformation(storageconnection,tempwwn):
    tparhost=''
    tparvolumes=''
    tparwwn=''
    tparlun=''

    stdin, stdout, stderr = storageconnection.exec_command('showvlun')
    lis=stdout.readlines()
    for i in lis[2:]:
       #print i.split()[3]
      try:
        #to ignore all unfilled data in the end
        if len(i.split()) >= 6:
         if i.split()[3]==tempwwn:
            #print i.split()

            tparhost=tparhost+"\n"+i.split()[2]
            tparvolumes=tparvolumes+"\n"+i.split()[1]
            tparwwn=tparwwn+"\n"+i.split()[3]
            tparlun=tparlun+"\n"+i.split()[4]

      except IndexError:
        print 'Error'

    return tparhost,tparvolumes,tparwwn,tparlun




