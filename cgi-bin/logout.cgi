#!/usr/bin/python
print "Content-type:text/html\n"
import cgi, cgitb, commands
cgitb.enable()

print '<script>alert("Logged Out")</script>\n'
print '<META HTTP-EQUIV=refresh CONTENT="1;URL=http://192.168.1.100/login.html">\n'
