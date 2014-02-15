__author__ = 'Arun'


def getWinHostName(con):
    for ios in con.Win32_ComputerSystem():
        var= ios.DNSHostName
    return var
def getWinOS(con):
    for ios in con.Win32_OperatingSystem():
        var= ios.NAME
    return var
def getWinModel(con):
    for ios in con.Win32_ComputerSystem():
        var= ios.Model
    return var
