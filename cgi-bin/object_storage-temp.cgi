#!/usr/bin/python

import cgi, cgitb, os, commands

cgitb.enable()

print "Content-type: text/html\n\n";

form=cgi.FormContent()
#size = '1'
#name = 'thin_client3'
size=form['size'][0]
name=form['name'][0]
print commands.getstatusoutput('sudo lvcreate -V {}G --name {}  vg_thin/tp_knowhere'.format(size,name))
print commands.getstatusoutput('sudo mkfs.xfs  /dev/vg_thin/{} ' .format(name))

print commands.getstatusoutput('sudo mkdir  /mnt/{}'.format(name))
print commands.getstatusoutput('sudo mount  /dev/vg_thin/{}  /mnt/{}'.format(name,name))
print commands.getstatusoutput('sudo echo "/mnt/{} *(rw,no_root_squash)" >> /etc/exports'.format(name))
print commands.getstatusoutput("sudo systemctl restart nfs-server")


f=open("/var/www/cgi-bin/staas_access.py" , mode= "w")
f.write("#!/usr/bin/python \n")
f.write("import commands \n")
f.write("commands.getstatusoutput('sudo systemctl restart nfs-utils')\n")
f.write("commands.getstatusoutput('sudo mkdir /media/{}')\n".format(name))
f.write("commands.getstatusoutput('sudo mount 192.168.1.100:/mnt/{} /media/{}')".format(name,name))
f.close()
#commands.getstatusoutput("sudo tar -cvf staas_client.tar /var/www/cgi-bin/staassend.py")
#commands.getstatusoutput("sudo cp staas_access.py /var/www/html/")
print '<META HTTP-EQUIV=refresh CONTENT=\'0;URL= http://192.168.1.100/cgi-bin/staas_access.py\'>\n'
