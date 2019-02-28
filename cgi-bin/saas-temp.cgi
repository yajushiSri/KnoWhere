#!/usr/bin/python

import  cgi,cgitb,os,time,random
from commands import getstatusoutput

cgitb.enable()


print "Content-Type:text/html"
print ""

data=cgi.FieldStorage()
#  recv software name from  services.html    
sware=data.getvalue('sware')

def make_tar():
	rdm = str(random.randint(1000, 9999))
	fwrite = "sudo echo -e 'sshpass -p redhat ssh -X root@192.168.122.1 {0}' >> /var/www/cgi-bin/{0}{1}.sh".format(sware,rdm)
	sh = getstatusoutput(fwrite)
	print sh


	getstatusoutput('sudo chmod a+x  /var/www/cgi-bin/{0}{1}.sh'.format(sware,rdm))
	#getstatusoutput('sudo tar -cvf  /var/www/cgi-bin/{0}{1}.tar /var/www/cgi-bin/{0}{1}.sh'.format(sware,rdm))
	#getstatusoutput('sudo mv /var/www/cgi-bin/{0}{1}.tar /var/www/html/'.format(sware,random))
	getstatusoutput('sudo mv {0}{1}.sh /var/www/html/down/'.format(sware,random))
	print '<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://192.168.1.11/down/{0}{1}.sh">\n'.format(sware,rdm)

make_tar()
