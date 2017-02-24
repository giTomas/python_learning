#!/usr/bin/python

import MySQLdb

db = MySQLdb.connect("localhost", "testuser", "test123", "testdb")
cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS employee")

sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

print 'table was created!'

db.close
