#!/usr/bin/python

def printInfo(arg1=11, *args):
    print arg1
    for arg in args:
        print arg
    return;

def printInfo2(*args):
    for arg in args:
        print arg
    return;

def printInfo3(arg=10):
    print arg
    return;

# printInfo(10)
# print '-' * 10
# printInfo()
# print '-' * 10
# printInfo(30, 20,50)
# print '-' * 10
# printInfo2(100)
# print '-' * 10
# printInfo2(5, 8, 99)
# print '-' * 10
# printInfo3()

# LAMBDAS

sum = lambda arg1, arg2: arg1 + arg2;
multiply = lambda arg1, arg2: arg1*arg2;

# print "LAMBDA functions"
# print "value 10 + 30 = ", sum(10, 30)
# print "value 30 + 50 = ", sum(30, 50)
# print "value 10 * 50 = ", multiply(10, 50)

# RETURN statement
