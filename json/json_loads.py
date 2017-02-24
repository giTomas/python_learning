#!/usr/bin/python

import json

json_data = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'

json_as_python_value = json.loads(json_data)


print json_as_python_value['name☺']
print json_as_python_value
