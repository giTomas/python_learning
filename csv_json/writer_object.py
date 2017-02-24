#!/usr/bin/python

import csv

output_file = open('output.csv', 'w')
output_writer = csv.writer(output_file)
output_writer.writerow(['spam', 'eggs', 'bacon', 'ham'])
output_writer.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
output_writer.writerow([1,2,3.171592,4])
output_file.close()
