#!/usr/bin/python

print "Let's practice everything."
print "You\n need to know \'bout escapes with \\ that do \n newlines \t tabs"

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "start point: %d" % start_point
print "%d beans, %d jars and %d crates" % (beans, jars, crates)

start_point = start_point / 10
print "%d beans, %d jars and %d crates" % secret_formula(start_point)
