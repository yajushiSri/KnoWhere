#!/usr/bin/python
import mysql.connector, cgi, cgitb, os
cgitb.enable()


print   "Content-type: text/html\n"


data=cgi.FieldStorage()
#  recv software name from  services.html    
username=data.getvalue('username')
password=data.getvalue('password')
#username='yajushi'
#password='yajushi'
connection_var = mysql.connector.connect( user = 'root', password = 'redhat', database = 'userDB')
cursor = connection_var.cursor()
query = ("SELECT password from users where username LIKE '" + username + "' ;")
cursor.execute(query)
rows = cursor.fetchall()
for var in rows:
    if var[0] == password:    
	print "Successful"
        print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.1.100/index.html\">\n"
    else:
        print '<script>alert("Authentication Error")</script>\n'
        print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.1.100/login.html\">\n"
    break
cursor.close()
connection_var.close()    
#if  username   ==   'yajushi' and password == 'yajushi':
#	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.1.100/index.html\">\n";

	

#else:
#	print '<script>alert("Authentication Error")</script>\n'
#	print '<META HTTP-EQUIV=refresh CONTENT="0;URL=http://192.168.1.100/login.html">\n'
