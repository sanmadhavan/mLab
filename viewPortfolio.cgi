#!/usr/bin/python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
import sys
sys.path.append ('/opt/mchain/lib')
from mortgageHtmlElements import *
import mchainlog
import cgi
from mchainUtil import *
from mchainDB import *
from mchainLib import *



logger = mchainlog.setup_custom_logger('root')
cgitb.enable()
form = cgi.FieldStorage()
loanNumber = (form.getvalue('loannumber'))
portfolio = form.getvalue("portfolio")
phase = form.getvalue("phase")
password = form.getvalue("password")


#-----------------------------------------------------------------------------
def fetchPassKey():
     customerName=fetchMortgageCustomer(loanNumber)
     if not customerName:
        print "<script language='Javascript'>"
        print "alert ('Invaid loan Number or unable to fetch portfolio information');"
        print "window.history.back();"
        print "</script>"
     else:
      divclassOuterContainer()
      print "<div id='chain' class='tableChain'>"
      print "<div id='chain' class='tableChain'>"
      print "\t<h4>Enter the passkey to view the public portfolio of %s<h4>" % (customerName)
      #print "\t<form name='pform' class='form-inline' action='loadProfile.py'>"
      print "\t<form name='pform' class='form-inline' action='loanProfile.cgi' method='post'>"
      print "\t\t<div class='form-group'>"
      print "\t\t\t<input type='hidden' name='portfolio' value=%s>" % (loanNumber)
      print "\t\t\t<input type='hidden' name='phase' value=%s>" % (phase)
      print "\t\t\t<input type='password' name='password' size='48' />"
      print "\t\t\t<button type='submit' class='btn btn-default'>View Portfolio</button>"
      print "\t\t</div>"
      print "\t</form>"
      print "</div>"


#-----------------------------------------------------------------------------
cgitb.enable()
htmlContentType()
htmlHeader("Portfolio")
uname="Portfolio"
sessionTime=""
divclassNavBarPlain(uname,sessionTime)
divclassPageLocator("")
divclassOuterContainer()
print "<div id='chain' class='tableChain'>"
fetchPassKey()
print "</div>"
divEnd("outerContainer")
htmlFooter()


