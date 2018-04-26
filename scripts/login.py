#!/usr/bin/python2

import cgi

print "content-type: text/html"

userName = cgi.FormContent()['uname'][0]
passWord = cgi.FormContent()['password'][0]


with open("/webcontent/database/record.txt") as f:
	for line in f:
		if line.split(":")[0] == userName and line.split(":")[1] == passWord:
			print 
			h = open("/webcontent/database/whoIsLoggedIn.txt",'w')
			h.write("{}:isLoggedIn".format(userName))
			h.close()
			print """
				 <script>
        			    if (confirm('Successful Login! Click Ok to proceed') == true)
                			window.location = '../login1.html' ;
            			    else
                			window.location = '../index.html' ;
        </script>

				"""

	
print 
print """
	<script>
	    if (confirm('No such user! Create account first OR Incorrect password/username') == true)
		window.location = '../register.html' ;
	    else
		window.location = '../index.html' ;
	</script>
      """
	
		
		 
	

