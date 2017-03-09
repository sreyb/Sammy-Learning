import os
import sys

''' opens excel but divides filename by spaces;
    file = "C:\\Users\\Public\\Documents\\Dropbox\\Etech Docs\\Weekly Updates\\Sammy\\Channel Transpose.xlsm"

    os.system('start excel.exe %s' % (file))'''

os.system('start excel.exe "C:\\Users\\Public_'
          '\\Documents\\Dropbox\\Etech Docs\\Weekly Updates\\Sammy_'
          '\\Channel Transpose.xlsm"')
