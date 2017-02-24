#!/usr/bin/python

import json

python_data = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}

json_string = json.dumps(python_data)
print json_string
