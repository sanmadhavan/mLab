#!/usr/bin/python
import cgi
import os
import sys
sys.path.append ('/opt/mchain/lib')
from mortgageHtmlElements import *
import mchainlog
logger = mchainlog.setup_custom_logger('root')

form = cgi.FieldStorage()
uname = form.getvalue("username")
password = form.getvalue("password")

passkey = "python"
# -----------------------------------------------------------------------------
def displayLandingPage():
    print "\t\t    <h2 style='text-align:center;'>Welcome to Bank</h2> <br> <br>"
    print "\t\t    <div class='container-fluid'>"
    print "\t\t    <div class='row'>"
    print "\t\t        <div class='col-lg-3 col-md-3 well' style='margin-right:10px;'>"
    print "\t\t            <div style='text-align:center;'><h3>Mortgage</h3></div>"
    print "\t\t            <div style='text-align:center;'><a href='/mortgage/mortgage-dashboard.cgi?showdboard=yes'><img src='images/icon_mortgage.png' alt='HTML5 Icon'style='width:128px;height:128px;'></a></div>"
    print "\t\t        </div>"
    print "\t\t        <div class='col-lg-1 col-md-1'></div>"
    print "\t\t        <div class='col-lg-3 col-md-3 well' style='height:223px;'>"
    print "\t\t            <div style='text-align:center;'><h3>Private Banking</h3></div>"
    print "\t\t            <div style='text-align:center;'><a href='#'><img src='images/icon_banking.png' alt='HTML5 Icon' style='width:128px;height:128px;'></a></div>"
    print "\t\t        </div>"
    print "\t\t        <div class='col-lg-1 col-md-1'></div>"
    print "\t\t        <div class='col-lg-3 col-md-3 well'>"
    print "\t\t            <div style='text-align:center;'><h3>Wealth</h3></div>"
    print "\t\t            <div style='text-align:center;'><a href='#'><img src='images/icon_wealth.png' alt='HTML5 Icon' style='width:128px;height:128px;'></a></div>"
    print "\t\t        </div>"
    print "\t\t   </div>"   
    print "\t\t   </div>"


# -----------------------------------------------------------------------------
def showDashboardPage():
    sessionTime="12:00:00"
    uname="Guest"
    divclassNavBar(uname,sessionTime)
    divclassPageLocator("")
    divclassOuterContainer()
    displayLandingPage()
    divEnd("outerContainer")
# -----------------------------------------------------------------------------

htmlContentType()
if not form:
    htmlHeader("Login Response")
    print "<script language='Javascript'>"
    print "alert ('Please provide login credentials');"
    print "window.document.location.replace ('login.cgi');"
    print "</script>"
elif form.has_key("username") and form["username"].value != "" and form.has_key("password") and form["password"].value == passkey:
    htmlHeader("Mortgage Dashboard")
    showDashboardPage()
    htmlFooter()
elif form.has_key("showdboard") and form["showdboard"].value == "yes":
    htmlHeader("Mortgage Dashboard")
    showDashboardPage()
    htmlFooter()
else:
    htmlHeader("Invalid Login")
    print "<script language='Javascript'>"
    if not password:
        print "alert ('Please provide password');"
    else:
        print "alert ('Incorrect Password');"
    print "window.document.location.replace ('login.cgi');"
    print "</script>"
    htmlFooter()







