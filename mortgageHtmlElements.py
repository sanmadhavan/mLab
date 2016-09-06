#!/usr/bin/python
def header(title):
    print "Content-type: text/html\n"

def htmlContentType():
        print "Content-type: text/html\n\n"
        print "<html>"
def throwError(msg):
        print "<script language='Javascript'>"
        print "alert ('%s');" % (msg)
	print "window.history.back();"
        print "window.document.location.replace ('login.cgi');"
        print "</script>"
def displaySearch():
    print "<div id='chain' class='tableChain'>" 
    print "\t<h4>Search customer by loan number:</h4>"
    print "\t<form class='form-inline' action='validateLoanNumber.py'>"
    print "\t\t<div class='form-group'>"
    print "\t\t\t<input type='text' name='loannumber' size='64' value=''/>"
    print "\t\t\t<button type='submit' class='btn btn-default'>Search</button>"
    print "\t\t</div>"
    print "\t</form>"
    print "</div>"

def htmlHeader(title):
        print "<head>"
        print "        <title>%s</title>" % (title)
	print "        <link rel='icon' type='image/vnd.microsoft.icon' href='images/mphasis1.png' />"
        print "        <link rel='shortcut icon' href='favicon.ico'/> "
        print "        <link rel='stylesheet' href='css/bootstrap.min.css'>"
        print "        <link rel='stylesheet' href='css/blockchain.css'>"
	print "	       <script src='js/jquery.min.js'></script>"
	print "        <link rel='stylesheet' href='razorflow_js/css/razorflow.min.css'/>"
        print "	       <script src='razorflow_js/js/jquery.min.js' type='text/javascript'></script>"
	print "        <script src='razorflow_js/js/razorflow.min.js' type='text/javascript'></script>"
        print "	       <script src='razorflow_js/js/razorflow.devtools.min.js' type='text/javascript'></script>"
	print "        <script src='js/bootstrap.min.js'></script>"
	print "        <style> #dashboard_target {width: 800px;}</style>"
#	print "	       <script src='https://www.amcharts.com/lib/3/ammap.js'></script>"
#	print "		<script src='https://www.amcharts.com/lib/3/maps/js/usaLow.js'></script>"
#	print "		<script src='https://www.amcharts.com/lib/3/themes/light.js'></script>"

	print "<style>"
	print "#chartdiv {\
		width	: 50%;\
		left	: 30%;\
		top	: 10%;\
		height	: 400px;\
	}"
	print "#loader {\
  position: absolute;\
  left: 50%;\
  top: 50%;\
  z-index: 1;\
  width: 150px;\
  height: 150px;\
  margin: -75px 0 0 -75px;\
  border: 16px solid #f3f3f3;\
  border-radius: 50%;\
  border-top: 16px solid #3498db;\
  width: 120px;\
  height: 120px;\
  -webkit-animation: spin 2s linear infinite;\
  animation: spin 2s linear infinite;\
}\
\
@-webkit-keyframes spin {\
  0% { -webkit-transform: rotate(0deg); }\
  100% { -webkit-transform: rotate(360deg); }\
}\
\
@keyframes spin {\
  0% { transform: rotate(0deg); }\
  100% { transform: rotate(360deg); }\
}\
.animate-bottom {\
  position: relative;\
  -webkit-animation-name: animatebottom;\
  -webkit-animation-duration: 1s;\
  animation-name: animatebottom;\
  animation-duration: 1s\
}\
@-webkit-keyframes animatebottom {\
  from { bottom:-100px; opacity:0 } \
  to { bottom:0px; opacity:1 }\
}\
@keyframes animatebottom { \
  from{ bottom:-100px; opacity:0 } \
  to{ bottom:0; opacity:1 }\
}\
/* Tooltip container */\
.tooltip {\
    position: relative;\
    display: inline-block;\
    border-bottom: 1px dotted black; /* If you want dots under the hoverable text */\
}\
/* Tooltip text */\
.tooltip .tooltiptext {\
    visibility: hidden;\
    width: 120px;\
    background-color: black;\
    color: #fff;\
    text-align: center;\
    padding: 5px 0;\
    border-radius: 6px;\
    /* Position the tooltip text - see examples below! */\
    position: absolute;\
    z-index: 1;\
}\
/* Show the tooltip text when you mouse over the tooltip container */\
.tooltip:hover .tooltiptext {\
    visibility: visible;\
}\
#myDiv {\
  display: none;\
  text-align: center;\
}\
</style>"
        print "</head>"
def divclassNavBarPlain(uname,logintime):
      print "	<body>"
      print "		<nav class='navbarplain navbar-inverse navbar-static-top borderBottom'>"
      print "		<div class='navbar-header'>"
      print "			<a class='navbar-brand' href='#'>"
      print "			<img src='images/mphasis_logo.png' class='brandLogoImage1'/>"
      print "			</a>"
      print "		</div>"
      print "		<div id='navbar'>" 
      print "		</div>"
      print "		</nav>"

def divclassNavBar(uname,logintime):
      print "	<body>"
      print "		<nav class='navbar navbar-inverse navbar-static-top borderBottom'>"
      print "		<div class='navbar-header'>"
      print "			<a class='navbar-brand' href='#'>"
      print "			<img src='images/mphasis_logo.png' class='brandLogoImage1'/>"
      print "			</a>"
      print "		</div>"
      print "		<div id='navbar'>" 
#	print "			<ul class='nav navbar-nav'>"
#	print "				<li><a href='#'>%s</a></li>" %(uname)
#	print "				<li class='dropdown'>"
#	print "					<a href='#' class='dropdown-toggle' data-toggle='dropdown' role='button' aria-haspopup='true' aria-expanded='false'>&nbsp;&nbsp;&nbsp; %s <span class='caret'></span></a>" %(uname)
#	print "					<ul class='dropdown-menu'>"
#	print "					<li><a href='#'>Link 1</a></li>"
#	print "					</ul>" 
#	print "				</li>"
#	print "			</ul>"
      if (uname != "Portfolio"):
	print "			<ul class='nav navbar-nav'>"
	print "				<li><a href='/mortgage/mortgage-landing.cgi?showdboard=yes'>Home</a></li>" 
	print "			</ul>"
	print "			<ul class='nav navbar-nav'>"
	print "				<li class='dropdown'>"
	print "					<a href='#' class='dropdown-toggle' data-toggle='dropdown' role='button' aria-haspopup='true' aria-expanded='false'>&nbsp;&nbsp;&nbsp; Dashboard <span class='caret'></span></a>"
	print "					<ul class='dropdown-menu'>"
	print "					<li><a href='/mortgage/mortgage-dashboard.cgi?showdboard=yes'>Mortgage</a></li>"
	print "					<li><a href='#'>Private Banking</a></li>"
	print "					<li><a href='#'>Wealth</a></li>"
	print "					</ul>" 
	print "				</li>"
	print "			</ul>"
	print "			<ul class='nav navbar-nav'>"
	print "				<li class='dropdown'>"
	print "					<a href='#' class='dropdown-toggle' data-toggle='dropdown' role='button' aria-haspopup='true' aria-expanded='false'>&nbsp;&nbsp;&nbsp; Chains <span class='caret'></span></a>"
	print "					<ul class='dropdown-menu'>"
	print "					<li><a href='/mortgage/mortgageChains.cgi'>Mortgage</a></li>"
	print "					<li><a href='#'>Private Banking</a></li>"
	print "					<li><a href='#'>Wealth</a></li>"
	print "					</ul>" 
	print "				</li>"
	print "			</ul>"
	print "			<ul class='nav navbar-nav alignRight'>"
	print "				<li><a href='#'>Logged in at %s</a></li>" %(logintime)
	print "			</ul>"
      
      print "		</div>"
      print "		</nav>"
def divclassPageLocator(linkname):
	return
	#print "		<div class='pageLocator'>"
	#print "			<span><a href='/mchain/chainids.cgi?'>Home</a></td></span>"
	#print "		</div>"
	#!!!print "			<span><a href='/mchain/btransactions.cgi?'>Home</a></td></span>"
	#if linkname:
	#	print "			<span class='active'>%s</span>" % (linkname)
	#print "		</div>"
def divclassOuterContainer():
	print "		<div class='outerContainer'>"
def divEnd(commentString):
	print "		</div> <!-- %s -->"% (commentString)
def htmlFooter():
	print "</body></html>"
	return
	print "<footer> "
#print "		Copyrights 2016. All Rights Reserved."
	print "			</footer>"
	print "</body></html>"

