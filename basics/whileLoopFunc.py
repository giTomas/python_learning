#!/usr/bin/python

from sys import argv
☻

def argvToNumbers(arguments):
    nuList = []
    arguments.pop(0)
    for i in arguments:
        nuList.append(int(i))
        # print i
    return nuList

# print numbers

def whileLoop(i, limit, increment):
    numbers = []
    while i < limit:
        print "At the top i is %d" % i
        numbers.append(i)

        i += increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "
    for num in numbers:
        print num
    return numbers

numbers = argvToNumbers(argv)
# whileLoop(int(argv[1]), int(argv[2]), int(argv[3]))
whileLoop(numbers[0], numbers[1], numbers[2])
