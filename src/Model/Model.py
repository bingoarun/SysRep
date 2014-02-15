class Model:
    _hostname=''
    #_credentials=['','']
    _type=''
    _os=''
    _ser_profile=''
    _location=''
    _primary_ip=''
    _ipaddr=''
    _macaddr=''
    _category=''
    _passcat=''
    _tparhost=''
    _tparvolumes=''
    _wwn=''
    _lun=''

    def __init__(self,_primary_ip,_category,_passcat,_hostname=None,_type=None,_os=None,_ser_profile=None,_location=None,_ipaddr=None,_macaddr=None,_tparhost=None,_tparvolumes=None,_wwn=None,_lun=None):
        self._hostname=_hostname
        #self._credentials=_credentials
        self._type=_type
        self._os=_os
        self._ser_profile=_ser_profile
        self._location=_location
        self._primary_ip=_primary_ip
        self._ipaddr=_ipaddr
        self._macaddr=_macaddr
        self._category=_category
        self._passcat=_passcat
        self._wwn=_wwn
        self._tparhost=_tparhost
        self._tparvolumes=_tparvolumes
        self._wwn=_wwn
        self._lun=_lun
    def __str__(self):
        return "Working fine for:"+self._hostname








