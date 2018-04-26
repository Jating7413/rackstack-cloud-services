#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"
print

fileData=cgi.FormContent()['file'][0]

fh=open('/webcontent/database/data.txt' , 'w')
fh.write(fileData)
fh.close()

f = open('/webcontent/database/name.txt' , 'r')
name = f.read()
f.close()

n = name.split('\n')
na = n[0]

g = open('/webcontent/database/port.txt' ,'r')
port = g.read()
g.close()

p = port.split('\n')
pa = p[0]

ip = commands.getoutput("sudo ifconfig enp0s3")
ipAdd = ip.split()
ipAddress = ipAdd[5]

launch = commands.getstatusoutput("sudo docker run -dit -p {}:80 --name {} apacheimg:v2".format(pa, na))
status = commands.getstatusoutput("sudo docker cp /webcontent/database/data.txt {0}:/var/www/html/index.html".format(na))
if status[0]==0:
	commands.getstatusoutput("sudo docker exec {} /usr/sbin/httpd".format(na))
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

	
		#banner {background: #666; height: 340px; padding: 20px; clear: both; background-image: url("../images/code.jpg"); color: white; border:3px solid black;}
		#banner form {color:white; }
		#left {float: left; width:565px; height: 340px; border: 3px solid white; color: white; background: #181818 ; border-radius:8px;   }
		#right {float: right; width: 565px; height: 340px; border: 3px solid white; color: white;     background: #000; border-radius:8px;}
		#right iframe {margin-left: 13px;}
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

		#ppp { text-align: center; font-family:verdana; padding:3px; margin:3px; }
		#styleContent2 {text-align: center; font-family:verdana;}
		#aq {text-align:center; font-family:verdana; text-decoration:none; color:white; margin-left:170px; border:2px solid #333; padding:10px; background-color:#333;	border-radius: 8px;}		
		/* #form {float: right; margin: 30px; font-family: arial;} */
	</style>



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
					<div id="left">
	"""
	print "<br>"
	print "<p id='ppp' >Website deployed successfully ..</p>"
	print "<p id='ppp'>Access your website from browser by entering :  {}:{} </p>".format(ipAddress,pa)
	print "<br><br><br><br>"
	print "<a id='aq' href='../sshinstance.html'>Click here to launch more</a>"
					
	print """			</div>
					<div id ="right">
						<iframe width="535" height="330" src="https://www.youtube.com/embed/5nJtIXWMdYg" frameborder="0" allowfullscreen>
						</iframe>
					
					</div>
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
	f = open("/webcontent/database/whoIsLoggedIn.txt" , 'r')
	name = f.read()
	f.close()

	g = open("/webcontent/database/whowhat.txt" , 'a')
	g.write("{}:{}:#\n".format(name,na))
	g.close()
	
	







