#!/usr/bin/python

def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def substract(a, b):
    print "SUBSTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Some math"

age = add(27, 5)
weight = substract(85, 5)
height = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, weight: %d, IQ: %d" % (age, height, weight, iq)

print "Puzzle:"

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print "That becomes ", what, "can you do it by hand?"
