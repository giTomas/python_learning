#!/usr/bin/python

import re

# str = 'an example word:cat!!'
#
# # 'r' python raw string
# match = re.search(r'word:\w\w\w', str)
#
# if match:
#     print 'found', match.group()
# else:
#     print 'did not find'

def check(x):
    if x != None:
        return x
    else:
        return 'value is None'

# r'string' zabrani tomu aby bol regex vyhodnoteny pythonom ako string s escapechars

match = re.search(r'iii', 'piiig')
print match.group()

match = re.search(r'igs', 'piig')
print match == None

match = re.search(r'..g', 'piig')
print match.group()

match = re.search(r'\d\d\d', 'p123g')
print check(match.group())

match = re.search(r'\w\w\w', '@@klm!')
print check(match.group())

print "\n \tRepetition \n"

word = 'piiiiig'
# '+' one or more occurence of preceeding char
match = re.search('i+', word)
print match.group()

# '+' match only first occurence
match = re.search('i+', word + 'iiii')
print match.group()

# \s* zero or more whitespace chars
t_string = '1  10 8'
match = re.search(r'\d\s*\d\s*\d\s*', t_string)
print match.group()

# ^ match start of he string
t_string = 'lalolol'
match = re.search(r'^a\w*', t_string)
print 'Not found', match == None
match = re.search(r'^l\w*', t_string)
print match.group()

print "\n \tRepetition \n"

#
# find email
#
t_str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', t_str)
print match.group()

## square brackets [] match chars in group, '+' mean one or more occurrences of char from group of chars in []
match = re.search(r'[\w.-]+@[\w.-]+', t_str)
print match.group()

## group extraction
print "\n \tGroup extraction \n"

reg_ex = r'([\w.-]+)@([\w.-]+)'
match = re.search(reg_ex, t_str)
print match.group(0)
print match.group(1)
print match.group(2)

## find all
print "\n \tFind all \n"

### return list
reg_ex = r'[\w.-]+@[\w.-]+'
t_str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
emails =  re.findall(reg_ex, t_str)
print emails

for email in emails:
    print email

### find all with group return tuple
print "\n \tFind all with groups\n"

reg_ex = r'([\w.-]+)@([\w.-]+)'
tuples =  re.findall(reg_ex, t_str)

for tuple in tuples:
    print tuple[0]
    print tuple[1]

reg_ex = r'(([\w.-]+)@([\w.-]+))'
tuples =  re.findall(reg_ex, t_str)
print tuples

for tuple in tuples:
    print tuple[0]
    print tuple[1]
    print tuple[2]

### Greedy non greeedy
print "\n \tGreedy non greedy\n"

html_str = '<h2>alef</h2>lolotrol<p>bejt</p>'

####Greedy
reg_ex = r'<.*>'
tags = re.findall(reg_ex, html_str)
print tags

###Non Greedy '?' extension

reg_ex = r'<.*?>'
tags = re.findall(reg_ex, html_str)
print tags

#### match everything between html tags and store three groups
reg_ex = r'((<.*?>)([\w\d]+)(</.*?>))'
units = re.findall(reg_ex, html_str)
print units

#Substitution
print "\n \tSubstitution\n"

t_str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
reg_ex = r'([\w.-]+)@([\w.-]+)'
replaced = re.sub(reg_ex, r'\1@yo-yo-dyne.com', t_str)
print replaced
