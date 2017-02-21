#!\usr\bin\python

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s" % (from_file, to_file)

# in_file = open(from_file)
# indata = in_file.read()

indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

# out_file = open(to_file, 'w')
# out_file.write(indata)
# out_file = open(to_file, 'w').write(indata)
open(to_file, 'w').write(indata)
    
print "Alright, all done."


# nie je treba ak je indata out_files na jeden riadok
# out_file.close()
# in_file.close()
