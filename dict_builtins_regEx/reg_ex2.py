#!/usr/bin/python

import re

t_str = 'mr Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

#netreba davat /s ako hranicu slova
# * 0 alebo viac vyskytov
# + 1 alebo viac vyskytov
# ? match 0 or more times

reg_ex = r'[\w]*[lL]+[\w]+'
lolo = re.findall(reg_ex, t_str)
print lolo
