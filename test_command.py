import os
import subprocess

f = os.popen('nmcli dev show | grep DNS')
a= f.read()
print(a[0], type(a))