#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"


cName = cgi.FormContent()['x'][0]

conStopStatus=commands.getstatusoutput("sudo docker kill {0}".format(cName))

if conStopStatus[0]  == 0:
        print "location:  manage.py"
        print
else:
        print "not removed"
