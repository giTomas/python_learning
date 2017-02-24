#!/usr/bin/python

import os, csv, errno

dir_name = 'header_removed'

# try create dir, if already esists script ignore error
# will ignore only this error other err will be reported
# try:
#     os.makedirs(dir_name)
# except OSError as exception:
#     if exception.errno != errno.EEXIST:
#         raise

# possibly better solutution
try:
    os.makedirs(dir_name)
except OSError:
    if not os.path.isdir(dir_name):
        raise


for csv_filename in os.listdir('.'):
    if not csv_filename.endswith('.csv'):
        continue

    print 'removing header from ', csv_filename

    csv_rows = []
    csv_file = open(csv_filename)
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if csv_reader.line_num == 1:
            continue
        csv_rows.append(row)

        csv_file = open(os.path.join(dir_name, csv_filename), 'w')
        csv_writer = csv.writer(csv_file)
        for row in csv_rows:
            csv_writer.writerow(row)
    csv_file.close()
