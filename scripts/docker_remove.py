#!/usr/bin/python2

import commands
import cgi

print "content-type: text/html"

cName = cgi.FormContent()['x'][0]

contRemStatus=commands.getstatusoutput("sudo docker rm -f {}".format(cName))

if contRemStatus[0]==0:
	print "location: manage.py"
	print 
	
else:
	print "naah"
