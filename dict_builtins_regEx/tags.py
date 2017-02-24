#!/urr/bin/python

import re

hash = {}
reg_ex = r'<([a-z]+)>(.*)</\1>'
fh = open('tags.txt')
for i in fh:
    res = re.search(reg_ex, i)
    print res.group(1) + ': ' + res.group(2)
    hash[res.group(1)] = res.group(2)

print hash
fh.close()
