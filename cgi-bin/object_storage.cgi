#!/usr/bin/python

import cgi, cgitb, os, commands, sys

cgitb.enable()

print "Content-type: text/html\n\n";

#form=cgi.FormContent()
#size = '1'
#name = 'thin_test001'
#size = '1'
#name=form['name'][0]
data=cgi.FieldStorage()
name=data.getvalue('name')
size=data.getvalue('size')

print commands.getstatusoutput('sudo lvcreate -V {}G --name {}  vg_thin/tp_knowhere'.format(size,name))
print commands.getstatusoutput('sudo mkfs.xfs  /dev/vg_thin/{}'.format(name))

print commands.getstatusoutput('sudo mkdir  /mnt/{}'.format(name))
print commands.getstatusoutput('sudo mount  /dev/vg_thin/{}  /mnt/{}'.format(name,name))
print commands.getstatusoutput('sudo echo "/mnt/{} *(rw,no_root_squash)" >> /etc/exports'.format(name))
#os.system(" exportfs -arv" )
print commands.getstatusoutput("sudo systemctl restart nfs")


f=open("/var/www/cgi-bin/staas_access.py","w")
f.write("#!/usr/bin/python2.7 \n")
f.write("import commands \n")
#f.write("commands.getstatusoutput('sudo systemctl restart nfs-utils')\n")
f.write("commands.getstatusoutput('sudo mkdir /media/{}')\n".format(name))
f.write("commands.getstatusoutput('sudo mount 192.168.1.100:/mnt/{} /media/{}')".format(name,name))
f.close()
commands.getstatusoutput("sudo tar -cvf staas_client.tar staas_access.py")
commands.getstatusoutput("sudo mv /var/www/cgi-bin/staas_client.tar /var/www/html/")
print '<META HTTP-EQUIV=refresh CONTENT=\'0;URL= http://192.168.1.100/staas_client.tar\'>\n'

