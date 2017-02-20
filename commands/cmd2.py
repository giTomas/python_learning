#!/usr/bin/python

import subprocess
import sys

cmd = 'netstat -p tcp'

p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)

while True:
    out = p.stderr.read(1)
# The sole value of types.NoneType. None is frequently used
# to represent the absence of a value, as when default
# arguments are not passed to a function.
    if out == '' and p.poll() != None:
        break
    if out != '':
        sys.stdout.write(out)
        sys.stdout.flush
