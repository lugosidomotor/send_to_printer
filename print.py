#/usr/bin/python

import os
import glob

list = glob.glob("*.pdf")

for i in list:
  print(i)

for i in list:
  os.system("lpr -P Samsung_M2020_Series '" + str(i) + "'")
