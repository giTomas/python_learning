#!usr/bin/python

hr = '\n' + ('-' * 10) + '\n'

def temp( var):
    print hr + var + hr


#dictionary formatting
hash = {}
hash['word'] = 'parresia'
hash['count'] = 40
s = 'We want %(count)d copies of %(word)s' % hash

temp(s)

#deletions

var = 6
del var

list = ['a', 'b', 'c']
del list[-1]
print list

dict = {'a': 1, 'b':2, 'c':3}
del dict['c']
print dict

#reading files
f = open('test.txt', 'rU')
lines = f.readlines()
print lines[0]
#
# for line in f:
#     print line,


f.close()
