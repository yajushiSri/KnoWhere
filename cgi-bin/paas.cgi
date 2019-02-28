#!/usr/bin/python

import  cgi,cgitb,os,commands,time

cgitb.enable()


print   "Content-type: text/html\n"


data=cgi.FieldStorage()
#  recv software name from  services.html    
software=data.getvalue('container')

print "Loading Container Service for Python Development"

print "<META HTTP-EQUIV=refresh CONTENT=\"2;URL=http://192.168.1.100/python-dev.sh\">\n";

	
