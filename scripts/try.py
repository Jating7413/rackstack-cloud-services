at the time of login 

f = open("/webcontent/database/user.txt" , 'w')
f.write(username)
f.close()

when instance engine is launched ::


f = open("/webcontent/database/user.txt" , 'r')
name = f.read()
f.close()

f = open("/webcontent/database/whowhat.txt" , 'w')
f.write("{}:".format(name))
f.close()

when basic ssh is launched ::

yaha pe hoga na 
containerName = cgi.FormContent()['conName'][1]

f = open("/webcontent/database/whowhat.txt" , 'a')
f.write(":{}".format(containerName))
f.close()

when webserver instance is launched ::

yaha pe bhi hoga ::
containerName1 = cgi.FormContent()['conName'][1]

f = open("/webcontent/database/whowhat.txt" , 'a')
f.write(":{}".format(containerName1))
f.close()

when customized is launched ::

SAME AS ABOVE

----

when manage is launched ::

f = open("/webcontent/database/whowhat.txt" , 'r')
entry = f.read()
f.close()

a = []

#ye step dekh lio pehle

a.append(entry.split(":"))

if a[0][0] == name:   #(name of user.. read from 1st file, just for verfication)
	print "<table border='9'>"
	print "<tr><th> Image name </th><th> Container name </th><th> Status </th><th> Stop container </th><th> Start container </th><th> Remove container </th> "
	count=1
	for i in commands.getoutput("sudo docker ps -a").split('\n'):
		if count == 1:
			count=count+1
			pass
		else:
			j = i.split()
			for sublist in a:
				if j[-1] in sublist:
					cStatus=commands.getoutput("sudo docker inspect {} | jq '.[].State.Status'".format(j[-1]))
					print "<tr> <td>" + j[1] + "</td>  <td>" + j[-1] + "</td> <td>" + cStatus + "</td> <td> <input value=' " + j[-1] + " ' type = 'button' onclick=stop(this.value) />  </td> <td> <input value= ' " + j[-1] + " ' type = 'button' onclick=start(this.value) /> </td> <td> <input value=' " + j[-1] + " ' type = 'button' onclick=rem(this.value) /> </td></tr>"

	print "</table>"

















