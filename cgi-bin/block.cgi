#!/usr/bin/python


import cgi, cgitb, os, sys, commands


cgitb.enable()

print "Content-type: text/html\n"

data =cgi.FieldStorage()
name=data.getvalue('name')
size=data.getvalue('size')																								
#s=cgi.FormContent()
#dname=s['name'][0]
#dsize=s['size'][0]
#dname = 'block6'
#dsize = '1'
print commands.getstatusoutput("sudo lvcreate -V {}G --name {} vg_thin/tp_knowhere ".format(size,name))

print commands.getstatusoutput("sudo touch /etc/tgt/conf.d/{}.conf".format(name))

print commands.getstatusoutput("sudo chmod 777 /etc/tgt/conf.d/{}.conf".format(name))

fp=open("/etc/tgt/conf.d/{}.conf".format(name),mode='w')
fp.write("<target {}>\n ".format(name))
fp.write("		backing-store /dev/vg_thin/{} \n".format(name))
fp.write("</target>")
fp.close()
print commands.getstatusoutput("sudo systemctl restart tgtd")

f=open("/var/www/cgi-bin/block_access.py",mode='w')
f.write("#!/usr/bin/python2.7 \n")
f.write("import commands \n")
#f.write("print commands.getstatusoutput('sudo yum install iscsi-initiator-utils -y')\n")
f.write("print commands.getstatusoutput('sudo iscsiadm --mode discoverydb --type sendtargets --portal 192.168.1.100 --discover')\n")
f.write("print commands.getstatusoutput('sudo iscsiadm --mode node --targetname {} --portal 192.168.1.100 --login')\n".format(name))
f.close()
commands.getstatusoutput("sudo tar -cvf block_client.tar block_access.py ")
commands.getstatusoutput("sudo mv block_client.tar /var/www/html/")
print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.1.100/block_client.tar\">\n"
