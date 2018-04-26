#!/usr/bin/python2

import sys
sys.stderr = sys.stdout
print "Content-Type: text/plain"
print

import cgi
import zipfile
import commands
import os

form = cgi.FieldStorage()

filefield = form['data']

#commands.getstatusoutput("sudo mv -r {} /root/Desktop".format(filefield.filename))

print "Filename:", filefield.filename

if filefield.file is not None and zipfile.is_zipfile(filefield.file):
	zfile = zipfile.ZipFile(filefield.file)
	print "Name list:\n\t",
	print "\n\t".join(zfile.namelist())
	print ZipFile.getinfo('12.txt')	





