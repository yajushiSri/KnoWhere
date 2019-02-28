#!/usr/bin/python

import  cgi,cgitb,os,commands,time

cgitb.enable()


print   "content-type:text/html"
print   ""

data=cgi.FieldStorage()
#  recv software name from  services.html    
software=data.getvalue('sware')

if  software   ==   'firefox' :
	print   "wait for  Web Browser "
	print "<META HTTP-EQUIV=refresh CONTENT=\"2;URL=http://192.168.1.100/saas/firefox.sh\">\n";
	
	
	
elif  software  ==   'gedit' :
	print   "wait for Text Editor "
	print "<META HTTP-EQUIV=refresh CONTENT=\"2;URL=http://192.168.1.100/saas/gedit.sh\">\n";
	

elif  software  ==   'bc' :
	print   "wait for  Calculator "
	print "<META HTTP-EQUIV=refresh CONTENT=\"2;URL=http://192.168.1.100/saas/bc.sh\">\n";
	
