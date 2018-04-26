#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"
print

a = cgi.FormContent()['html'][0]

print "{0}".format(a)

