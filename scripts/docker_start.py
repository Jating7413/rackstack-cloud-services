#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"


cName = cgi.FormContent()['x'][0]

conStartStatus=commands.getstatusoutput("sudo docker start {0}".format(cName))
serviceStart = commands.getstatusoutput("sudo docker exec {0} /usr/sbin/httpd".format(cName))

if conStartStatus[0]  == 0:
        print "location: manage.py"
        print
else:
        print "not removed"

