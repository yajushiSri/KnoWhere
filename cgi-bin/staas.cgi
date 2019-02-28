#!/usr/bin/python

import  cgi,cgitb,os,commands,time

cgitb.enable()


print "Content-type: text/html\n\n";

data=cgi.FieldStorage()
#  recv software name from  services.html    
store=data.getvalue('storage')

if store   ==   'object' :
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.1.100/object_storage.html\">\n";
#	print "Location: http://192.168.1.11/object_storage.html"
#	print	"<a href='http://192.168.1.6/Cloud/staas/object.html'>"
#	print	"Click here for Object Storage Services "
#	print	"</a>"
	
elif  store  ==   'block' :
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.1.100/block_storage.html\">\n";
	

