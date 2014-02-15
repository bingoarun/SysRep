__author__ = 'Arun'

def getWinMacAddr(con):
    var=''
    for interface in con.Win32_NetworkAdapterConfiguration (IPEnabled=1 ) :
        var= var+interface.MACAddress+"\n"
    return var
def getWinIPAddr(con):
    var=''
    for interface in con.Win32_NetworkAdapterConfiguration (IPEnabled=1 ) :
        for ip_address in  interface.IPAddress:
            var= var+ip_address+"\n"
    return var


