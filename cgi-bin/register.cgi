#!/usr/bin/python

import mysql.connector, cgi, cgitb
cgitb.enable()

print   "Content-type: text/html\n"


data=cgi.FieldStorage()
#  recv software name from  services.html    
username=data.getvalue('username')
password=data.getvalue('password')
first_name = data.getvalue('first_name')
last_name = data.getvalue('last_name')

connection_var = mysql.connector.connect( user = 'root', password = 'redhat', database = 'userDB')
cursor = connection_var.cursor()
query = ("SELECT password from users where username LIKE '" + username + "' ;")
cursor.execute(query)
rows = cursor.fetchall()
count = cursor.rowcount
cursor.close()
if count == 0:
    cursor = connection_var.cursor()
    query = ("insert into users (username, password, first_name, last_name) values ('" + username + "' , '" + password + "' , '" + first_name + "' , '"+ last_name + "' );")
    cursor.execute(query)
    connection_var.commit()
else:
    print "Username already taken\n"
print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.1.100/login.html\">\n"
cursor.close()
connection_var.close()
