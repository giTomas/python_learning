#!/usr/bin/python

class Test(object):
        count = 0
        __count = 0

        def addCount(self):
            self.count += 1

        def addSecretCount(self):
            self.__count += 1

        def showSecretCount(self):
            return self.__count

t = Test()
t.addCount()
t.addCount()
t.addSecretCount()
t.addSecretCount()
t.addSecretCount()

print t.count

print t.showSecretCount()
