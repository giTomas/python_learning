# x = int(raw_input('Some Number?  '))
# print "%d + 13 is %d" % (x, x + 13)

name = raw_input("Name?  ")
question = "%s, how old are you? " % name
age = raw_input(question)
answer = "You are %s and you are %s years old" % (name, age)
print answer
