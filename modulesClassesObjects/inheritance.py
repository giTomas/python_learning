#! /usr/bin/python

class Parent:
    parentAttr = 100

    def __init__(self):
        print 'Calling parent constructor'

    def parentMethod(self):
        print 'Calling parent method'

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "Parent attribute: ", Parent.parentAttr

class Child(Parent):
    def __init__(self):
        print "Calling child constructor"

    def childMethod(self):
        print "Calling child method"

print "-" * 10

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()

print issubclass(Child, Parent)
print isinstance(c, Child)

print "-" * 10

class Parent2:
    def myMethod(self):
        print 'Parent method'

class Child2(Parent2):
    def myMethod(self):
        print 'Child method'

c2 = Child2()
# c2.myMethod()

# secret

class JustCounter:
    __secretCounter = 0

    def count(self):
        self.__secretCounter += 1

    def showCounter(self):
        print self.__secretCounter

counter = JustCounter()
counter.count()
counter.count()
# print counter.__secretCounter
counter.showCounter()
