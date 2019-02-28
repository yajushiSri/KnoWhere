#!/usr/bin/python2.7 
import commands 
print commands.getstatusoutput('sudo iscsiadm --mode discoverydb --type sendtargets --portal 192.168.1.100 --discover')
print commands.getstatusoutput('sudo iscsiadm --mode node --targetname final_test004 --portal 192.168.1.100 --login')
