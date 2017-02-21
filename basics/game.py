#!/usr/bin/python

print "You enter a dark room with two doors. Do you go throught #1 or #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating cheese cake. What will you do?"
    print "1. Take the cake."
    print "2. Screan at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == '2':
        print "The bear eats your leggs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear run away" % bear

elif door == "2":
    print "You stare into endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yellling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by mind of jello Good Job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good Job!"

else:
    print "You stumble around and fall on knife and die. Good Job!"
