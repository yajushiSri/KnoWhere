#!/usr/bin/python2.7 
import commands 
commands.getstatusoutput('sudo mkdir /media/final_test003')
commands.getstatusoutput('sudo mount 192.168.1.100:/mnt/final_test003 /media/final_test003')