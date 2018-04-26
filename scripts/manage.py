#!/usr/bin/python2

import cgi
import commands

print "content-type:  text/html"
print 

a = open("/webcontent/database/whoIsLoggedIn.txt" , 'r')
name = a.read()
a.close()

f = open("/webcontent/database/whowhat.txt" , 'r')
entry = f.read()
f.close()

b = entry.split("\n")
c = []
d = []

for line in b:
	c.append(line.split(":"))

for sublist in c:
	if name.split(":")[0] in sublist:
		d.append(sublist[2])		

print """

	<html>
	<head>
	<style type="text/css">
		html { font-family: Arial, Helvetica; color:#333;  }
		body { background:#ccc; margin: 0;	 }
		#container {width:1200px; margin:0 auto; background: #333; }
		#header {width:100%; height: 60 px ;border-bottom: 0px solid #c7c7c7; background: #333}
		#logo {float: left; width:80px; height: 40px; margin:10px; background: #ccc;}
		#logo img {float: left; width: 150px; height: 50px; border: 0px solid white; padding:0px;}
		#form {float: right; margin: 18px;font-family: arial;}
		#register {float:right; margin: 10px; color: white; font-size: 12px; padding-right: 10px; }
		#register p a {color:white; text-decoration: none;}
		/*#top_info {float: right; width: 20px; height: 40px; background: #666; border: 1px solid #c7c7c7; margin: 10px; }
		*/
	
		#navbar {height:20px; clear: both; }
		#navbar ul {margin:0px; padding: 0; list-style-type: none; }
		#navbar ul li {padding: 0px; float: left; font-family: Helvetica; margin-right: 0px; position: relative;}
		#navbar ul li:hover > ul {display: block;}
		#navbar ul li a {font-size: 13px;float: left;text-align: center; padding: 10px 10px 10px 10px; display: block; text-decoration: none; color:lightgrey; width:280px; font-family: verdana; font-weight: bold;}
		#navbar ul li a:hover { color:#333; background-color: lightgrey;}
		#navbar ul ul {clear:both; display: none; position: absolute;}
		#navbar ul ul li {padding: 0px;  font-family: Helvetica; margin-right: 0px; background-color: #333;}

		#footer ul {margin:0px; padding:0px; list-style-type: none; }
		#footer ul li {float: left; font-family: Verdana; margin-right: 40px; margin-left: 40px; margin-bottom: 40px;  display: block;}
		#footer ul li a {text-decoration: none; color:white; font-size: 13px;}

	
		#banner {background: #666; height: 470px; padding: 20px; clear: both; background-image: url("../images/code.jpg"); color: white; border:3px solid black;}
		#banner form {color:white; }
	
		#footer {padding: 20px; clear: both; color:white;}
	 	#banner img {height: 220; padding-right:0px; padding-left: 0px; border: 1px solid #ddd; border-radius: 12px; padding: 5px; }
		#banner img:hover {box-shadow: 0 0 2px 1px rgba(0, 140, 186, 0.5); opacity: 2; border-width: 3px; }

		#banner2 {background: black; height: 0px;  clear: both; background-image: url("..images/banner4.jpg"); border:3px solid black;}
		#banner2 p {text-align: center; color: white; margin:0; line-height: 50px; font-family: verdana; }
		#banner2 p a {text-decoration: none; color: white;}
		#banner2 p:hover {clear:both; color:black; font-size: 20px; transition: font-size 2s; }
		#banner2 img {height: 220; padding-right:30px; padding-left: 10px; border: 1px solid white;}
	
		#banner3 {background: #666; height: 100px; padding: 20px; clear: both; background-image: url("../images/code.jpg"); color: white; border:3px solid black;}
		#banner3 img {height: 220; padding-right:0px; padding-left: 0px; border: 1px solid #ddd; border-radius: 12px; padding: 5px;  }
		#banner3 img:hover {box-shadow: 0 0 2px 1px rgba(0, 140, 186, 0.5); opacity: 2; border-width: 3px;}

		table {border-collapse: collapse; width:100%; color:white; font-size:16px;}
		table th td {border: 3px solid white;}
		th td {border-bottom: 1px solid #ddd;}
		table tr {height:10px; background-image: url('../images/code.jpg')}
		table tr:hover {background-color: #181818;}		
		table td {text-align:center; height:30px; border:3px solid white;}		
		#tt{ height: 45px; border: 5px solid white;}
		#btn {color:white; background-color: #131313; width:140px; height:40px; cursor:pointer; margin:10px; border-radius: 8px; border:2px solid white; font-size:16px; }
		#btn:hover {background-color: black; }
		#p {font-family:verdana; font-weight:bold; text-align:center;}
		/* #form {float: right; margin: 30px; font-family: arial;} */
	</style>

	 <script>
		function rem(mycname)
		{
		if(confirm('Are you sure you want to delete instance ??')== true)
		document.location='docker_remove.py?x=' + mycname;
		else
		document.location='manage.py';
		}

		function stop(mycname)
		{
		document.location='docker_stop.py?x=' + mycname;
		}

		function start(mycname)
		{
		document.location='docker_start.py?x=' + mycname;
		}

	</script>

	</head>
	<body>
		<!--Container -->
		<div id="container">
			<!-- Header -->
			<div id ="header">
				<div id="logo">
					<a href="index.html"> <img src="../images/logo.png" /> </a>

				</div>
				<!--<div id="top_info"> -->
			
				<div id="navbar">
					<ul>
						<li><a href="#">Why RackStack</a></li>
						<li><a href="#">Services</a>
							<ul>
								<br><br>
								<li><a onclick="nologin()">RackStack-SS</a></li>
								<li><a onclick="nologin()">RackStack-RSS</a></li>
								<li><a onclick="nologin()">Note-PAD</a></li>
								<li><a onclick="nologin()">Nomad-OS</a></li>
							</ul>
						</li>
						<li><a href="#">Blog</a></li>
						<li><a href="#">Support</a></li>
					</ul> 
				</div>

			</div>
			<!-- Content Area -->
			<div id="content_area">
				<div id="banner">
					
	"""
print "<p id='p'> Manage your launched Instances </p>"
print "<table border='3'>"
print "<tr><th id='tt'> Image name </th><th id='tt'> Name of Instance </th><th id='tt'> Status </th><th id='tt'> Stop instance </th><th id='tt'> Start instance </th><th id='tt'> Remove instance </th> "
count=1
for i in commands.getoutput("sudo docker ps -a").split('\n'):
	if count == 1:
		count=count+1
		pass
	else:
		j = i.split()
		if j[-1] in d:
			cStatus=commands.getoutput("sudo docker inspect {} | jq '.[].State.Status'".format(j[-1]))
			print "<tr> <td>" + j[1] + "</td>  <td>" + j[-1] + "</td> <td>" + cStatus + "</td> <td> <input id='btn' value=' " + j[-1] + " ' type = 'button' onclick=stop(this.value) />  </td> <td> <input id='btn' value= ' " + j[-1] + " ' type = 'button' onclick=start(this.value) /> </td> <td> <input id='btn' value=' " + j[-1] + " ' type = 'button' onclick=rem(this.value) /> </td></tr>"

print "</table>"

print """
					
				</div>
				<div id="banner2">
				
				</div>

				<div id="banner3">
				
				</div>
				<!--
				<div id="left_col">Left </div>
				<div id="right_col">Right</div>
				-->
			</div>

			<div id="footer">
				<ul>
					<li><a href="#">Contact</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| </li>
					<li><a href="#">Feedback</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|</li>
					<li><a href="#">About Us</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|</li>
					<li><a href="#">Pricing</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|</li>
					<li><a href="#">Support</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</li>
			
				</ul>
			</div>
		</div>
	</body>


	</html>
	""" 
	




