from distutils.core import setup
import py2exe
setup(
    name='pyHP',
    version='1.0',
    packages=['src', 'src.Main', 'src.Model', 'src.ExcelManager', 'src.ConnectionManager',
              'src.InformationManager', 'src.InformationManager.ESXInformationManager',
              'src.InformationManager.HPUXInformationManager', 'src.InformationManager.TPARInformationManager',
              'src.InformationManager.LinuxInformationManager', 'src.InformationManager.WindowsInformationManager'],
    install_requires=[
    "paramiko >= 1.10.0",
    "WMI >= 1.4.0",
    "XlsxWriter >= 0.4.0",
    "enum >= 0.4.0",
    "pycrypto >= 2.0.0",
    "xlrd >= 0.8.0"],
    url='',
    license='',
    author='Ciss',
    author_email='',
    description='',
    console=['src\SysRep.py']

)
