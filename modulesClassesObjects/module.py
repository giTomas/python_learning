#!/usr/bin/python

def meta():
    print "Couple of letters"

saying = "Soon I will walk out."

class MyStuff(object):

    def __init__(self):
        self.glum = "Something"

    def meta(self):
        print "Another few meanigless letters"

thing = MyStuff()
print thing.glum
thing.meta()
