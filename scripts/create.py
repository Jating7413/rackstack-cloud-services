#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"
print "" 

username = cgi.FormContent()['Username'][0]
size = cgi.FormContent()['size'][0]
ip = cgi.FormContent()['ipAddress'][0]
password = cgi.FormContent()['Password'][0]

#print(username)

hostentry='[{2}]\n{0}    ansible_ssh_user=root    ansible_ssh_pass={1}\n'.format(ip,password,username)

fh = open("/webcontent/database/inventory" , 'a')
fh.write(hostentry)
fh.close()

ipa = commands.getoutput("sudo ifconfig wlan0")
# ipAdd = ipa.split()
# ipaddress = ipAdd[5]
ipaddress = ipa.split()[6].split(":")[1]


#entry='---\n- hosts: me\n  tasks:\n      - lvol:\n          vg: "/dev/vgcloud"\n          lv: "{0}-lv1"\n          size: "{1}"\n      - filesystem:\n         fstype: ext4\n         dev: "/dev/vgcloud/{0}-lv1"\n      - file:\n          path: "/object/{0}-lv1"\n          state: directory\n      - mount:\n          path: "/object/{0}-lv1"\n          src: "/dev/vgcloud/{0}-lv1"\n          fstype: ext4\n          state: mounted\n\n- hosts: {0}\n  tasks:\n     - file:\n         path: "/media/{0}"\n         state: directory\n     - mount:\n          path: "/media/{0}"\n          src: "{2}:/object/{0}-lv1"\n          fstype: nfs\n          state: mounted\n'.format(username,size,ipaddress)

entry='---\n- hosts: me\n  sudo: True\n  tasks:\n      - lvol:\n          vg: "/dev/vgcloud"\n          lv: "{0}-lv1"\n          size: "{1}"\n      - filesystem:\n         fstype: ext4\n         dev: "/dev/vgcloud/{0}-lv1"\n      - file:\n          path: "/object/{0}-lv1"\n          state: directory\n      - mount:\n          path: "/object/{0}-lv1"\n          src: "/dev/vgcloud/{0}-lv1"\n          fstype: ext4\n          fstab: /webcontent/database/mountEntry.txt\n          state: mounted\n\n- hosts: {0}\n  tasks:\n     - file:\n         path: "/media/{0}"\n         state: directory\n     - shell: "mount -t nfs -o nfsvers=3 {2}:/object/{0}-lv1 /media/{0}"'.format(username,size,ipaddress)


#print(entry)

f = open("/webcontent/database/create.yml" , 'w')
f.write(entry)
f.close()

shareentry='/object/{0}-lv1         {1}(rw,no_root_squash)\n'.format(username,ip)

fh = open("/etc/exports" , 'a')	
fh.write(shareentry)
fh.close()

commands.getstatusoutput("sudo systemctl restart nfs")

new=commands.getstatusoutput("sudo ansible-playbook -i /webcontent/database/inventory /webcontent/database/create.yml")
if new[0]==0:

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

				#styleContent { text-align: center; font-family:verdana; padding:3px; margin:3px; }
				#styleContent2 {text-align: center; font-family:verdana;}
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
	print "<p id='styleContent'>"
	print "The disk of space {} is mounted successfully on your media folder with name {}".format(size,username)
	print "<br><br>"
	print "</p>"
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
else:
	print "naah"

#Write the entry of the new user and his dir size in a database file
ent = '{}:{}\n'.format(username,size)
db = open("/webcontent/scripts/database/db.txt" , 'a' )
db.write(ent)
db.close()

