# !/usr/bin/python

dict = {}
dict['b'] = 'beta'
dict['o'] = 'omega'
dict['a'] = 'alpha'

print 'print keys in random order'
for key in dict.keys():
    print key

for key in dict:
    print key

print 'get keys list'
print dict.keys()

print 'get list values'
print dict.values()

print 'accesing each key/value in alp order'
for key in sorted((dict.keys())):
    print key, dict[key]

print 'dict key value tuple'
print dict.items()

for k, v in dict.items():
    print k, '>', v
