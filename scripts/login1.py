#!/usr/bin/python2
import cgi
import commands

print "content-type: text/html"

userName = cgi.FormContent()[uname][0]
passWord = cgi.FormContent()[password][0]
#UID = cgi.FormContent()[userid][0]

with open("/webcontent/database/record.txt" , 'r') as f:
	for line in f:
		if line.split(":")[0] == userName and line.split(":")[2] == passWord
			print "location: ../login1.html"
			print ""
		else:
			print "<script> alert('Wrong username or ID.. Try again') </script>"
			print "location: ../index.html"
			print ""


"""
with open("/etc/passwd" , 'r') as f:
	for line in f:
		if line.split(":")[0] == userName and line.split(":")[2] == UID
			print "location: ../login1.html"
			print ""
		else:
			print "<script> alert('Wrong username or ID.. Try again') </script>"
			print "location: ../index.html"
			print ""
"""
"""
status = commands.getstatusoutput("useradd {}".format(userName))
if status[0]==0:
	print "User successfully created.. Login"
else:
	print "Try again"
"""


