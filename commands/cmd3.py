#!/usr/bin/python

from sys import argv
from os import path
import subprocess
import datetime

td = datetime.date.today()

tn_str = str(datetime.datetime.now()).replace(' ', '_').replace(':','-')

# (script, path='/home/tomas/python') = syst.argv

def listDir(dir='/home/tomas/python'):
    cmd = 'ls -l' + ' ' + dir
    print "Command to run", cmd
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

    (output, err) = p.communicate()

    return output

c_output = listDir(argv[1])
# print c_output

# textFile = str(td) + '.txt'
textFile = str(tn_str) + '.txt'

if path.isfile(textFile):
    t = open(textFile)
    oldText = t.read()
    t.close()
else:
    pass


hr = "\n" + ("-" * 30) + "\n"
# print oldText + hr + c_output
target = open(textFile, 'w')
# target.write(oldText + hr + c_output)
target.write(hr + c_output)
target.close()
