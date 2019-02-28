#!/usr/bin/python

import mysql.connector

usrname = '' # Database user name
passwd = '' # Database password
host_url = '' # URL of SQL server
dbname = '' # Name of the database

input_usr_name = '' #input username from the HTML
input_usr_passwd = '' #input password from the HTML

connection_var = mysql.connector.connect(user = usrname, password = passwd, 
        host = host_url, database = dbname)

cursor = connection_var.cursor()
query = ("SELECT password FROM users WHERE username like " + input_usr_name)
cursor.execute(query)
for var in cursor:
    if var == input_usr_passwd:
        #Execute authentication successful code
cursor.close()
connection_var.close()
