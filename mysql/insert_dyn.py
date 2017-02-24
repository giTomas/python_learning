#!/usr/bin/python

import MySQLdb

db = MySQLdb.connect('localhost', 'testuser', 'test123', 'testdb')
cursor = db.cursor()

sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
         LAST_NAME, AGE, SEX, INCOME) \
         VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
         ('Lol', 'Trol', 105, 'M', 4900)

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()
