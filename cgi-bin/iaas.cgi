#!/usr/bin/python

import cgi, cgitb, os, commands

cgitb.enable()

print "Content-type: text/html \n\n"

#data=cgi.FieldStorage()
##############################################################
name= 'cent_os5'
ram= '512'
core= '1'
port= '8991'
machine_id= 'first'
#name=data.getvalue('os_name')
#ram=data.getvalue('ram')
#core=data.getvalue('vcpu')
#port=data.getvalue('port')
#machine_id=data.gevalue('name')
#############################################################
#install_machine=commands.getstatusoutput("sudo virt-install --graphics vnc,listen=192.168.1.100,port={} --cdrom /var/lib/libvirt/images/CentOS-7-x86_64-Minimal-1810.iso --disk none  --memory {} --vcpus {} --name {} ".format(port,ram,core,name))

vnc_start=commands.getstatusoutput("websockify -D --web=/usr/share/novnc --cert=/etc/pki/tls/certs/novnc.pem 6080 localhost:5901".format(port))

#print install_machine
print vnc_start
