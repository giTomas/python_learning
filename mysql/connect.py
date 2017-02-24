#!/usr/bin/python

import MySQLdb

db = MySQLdb.connect("localhost", "testuser", "test123", "testdb")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data  = cursor.fetchone()
print "Database version : %s" % data
db.close()
