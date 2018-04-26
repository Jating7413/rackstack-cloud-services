#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"
print

a = cgi.FormContent()['cCode'][0]

f = open("/webcontent/database/user2.c" , 'w')
f.write(a)
f.close()

commands.getstatusoutput(" sudo chmod +x /webcontent/database/user2.c ")
commands.getoutput("sudo gcc -o user2 /webcontent/database/user2.c")
output =  commands.getoutput("sudo ./user2 ")

print """
<html>
<head>
<style type="text/css">
	html { font-family: Arial, Helvetica; color:#333;  }
	body { background:#ccc; margin: 0;	 }
	#container {width:1200px; margin:0 auto; background: #333; }
	#header {width:100%; height: 60px ;border-bottom: 0px solid #c7c7c7; background: #333}
	#logo {float: left; width:80px; height: 40px; margin:10px; background: #ccc;}
	#logo img {float: left; width: 150px; height: 50px; border: 0px solid white; padding:0px;}
	#form {float: right; margin: 18px;font-family: arial;}
	#register {float:right; margin: 10px; color: white; font-size: 12px; padding-right: 10px; }
	#register p a {color:white; text-decoration: none;}
	/*#top_info {float: right; width: 20px; height: 40px; background: #666; border: 1px solid #c7c7c7; margin: 10px; }
	*/
	#footer ul {margin:0px; padding:0px; list-style-type: none; }
	#footer ul li {float: left; font-family: Verdana; margin-right: 40px; margin-left: 40px; margin-bottom: 40px;  display: block;}
	#footer ul li a {text-decoration: none; color:white; font-size: 13px;}
	#navbar {height: 20px; clear: both; }
	#navbar ul {margin:0; padding: 0; list-style-type: none; }
	#navbar ul li {padding: 0px; float: left; font-family: Helvetica; margin-right: 0px; position: relative;}
	#navbar ul li:hover > ul {display: block;}
	#navbar ul li a {font-size: 13px;float: left;text-align: center; padding: 10px 10px 10px 10px; display: block; text-decoration: none; color:lightgrey; width:280px; font-family: verdana; font-weight: bold;}
	#navbar ul li a:hover { color:#333; background-color: lightgrey;}
	#navbar ul ul {clear:both; display: none; position: absolute;}
	#navbar ul ul li {padding: 0px;  font-family: Helvetica; margin-right: 0px; background-color: #333;}
	#textstyle {border-radius: 6px; height: 25px; border:0px;} 
	#submit {background-color:#333; color:#fff; border:2px solid white; width:170px; height: 30px; border-radius: 8px; font-family: verdana;  margin-top: 10px; cursor: pointer; background-image: url("../images/code.jpg");}
	#banner {background: #666; height: 470px; padding: 20px; clear: both; background-image: url("../images/code.jpg"); border:7px solid black;}
	#banner form textarea {background-color: black; color: white; margin-bottom: 5px; border:3px solid white; opacity: 0.7;}
	#left_col {float: left; width:552px; padding:20px; height: 150px; border: 1 px solid white; color: #FFF;margin-top: 5px; margin-left:5px; background: #000;}
	#right_col {float: right; width: 552px; height: 150px; border: 1 px solid white; color: #FFF; padding: 20px; background: #000; margin-top: 5px; margin-right: 5px;}
	#right_col img {float: right;}
	#footer {padding: 20px; clear: both; color: white;}
	#banner p {color:white; font-size: 22px; font-family: verdana; margin-top: 0px; text-align: left;}
	#out {height:340px; border:4px solid black; background-color: #181818; color:white; font-size:14px; border-radius: 8px;}	
	#btn7 {margin-top:20px; width:200px; height:37px; cursor:pointer; border:3px solid black; color:white; background-image: url("../images/code.jpg"); border-radius:8px; }
	/* #form {float: right; margin: 30px; font-family: arial;} */
</style>

<script type="text/javascript"> 
function nologin()
{
	alert("Login to use Services");
}
function goback()
{
	window.history.back();
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

				<p> Output goes here </p>
				<div id="out">

"""
print "<pre>"
print output
print "</pre>"
print """		
				</div>
				<button id="btn7" onclick="goback()"> Back to your Code </button>
			</div>
			<!--
			<div id="left_col">
				
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Benefits of creating a free account on RackStack :
				<ul>
				<li>Free access of Storage upto 10GB</li>
				<li>Free access of Raw Storage upto 10GB</li>
				<li>Unlimited Instances of basic configuration (RAM : 500MB, HD : 10GB)</li>
				<li>Free access to Coding Platform</li>
				<li>Launch complete GUI based VM of Linux Distros.</li>
				</ul>
			</div>
			<div id="right_col">
				<a href="#"><img src="images/right3.png" /></a>
				Now launch your virtual machine instances in just one click.
				Create your own customized containers and ssh to them from anywhere.
				<img src="images/right4.png" align="left" >
			</div>
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

