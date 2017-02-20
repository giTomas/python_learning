#!/usr/bin/python

import subprocess

# subprocess.call(["ls", "-la"])

p = subprocess.Popen("date", stdout=subprocess.PIPE, shell=True)

# Interact with process: Send data to stdin. Read data from stdout and stderr,
# until end-of-file is reached. Wait for process to terminate. The optional
# input argument should be a string to be sent to the child process, or None,
# if no data should be sent to the child.
(output, err) = p.communicate()

# preco je tu wait?
p_status = p.wait()
print "Command output : ", output
print "Command exit status/return code : ", p_status
