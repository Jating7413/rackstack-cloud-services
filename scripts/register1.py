#!/usr/bin/python2

import cgi
#import commands

print "content-type: text/html"
print

print "hey"
"""
username = cgi.FormContent()['username'][0]
first = cgi.FormContent()['first'][0]
last = cgi.FormContent()['last'][0]
PNum = cgi.FormContent()['phoneNum'][0]
email = cgi.FormContent()['email'][0]
"""
#print username
#print first
"""
with open("/etc/passwd") as f:
	for line in f:
		if line.split(":")[0] == username:
			print "<script> alert('Username already taken, try again with new username') </script>"
			exit()
		else:
			status = commands.getstatusoutput("sudo useradd {}".format(username))
			
if status[0] == 0:
	with open("/etc/passwd") as f1:
		for line in f:
			if line.split(":")[0] == username:
				id = line.split(":")[2]
				print "<script> alert('Account created successfully.. Your userID is {}'.format(id))</script>"
"""
