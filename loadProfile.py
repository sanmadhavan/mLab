#!/usr/bin/python
import sys
sys.path.append ('/opt/mchain/lib')
from mortgageHtmlElements import *
import mchainlog
logger = mchainlog.setup_custom_logger('root')

from mchainUtil import *
from mchainDB import *
from mchainLib import *

import cgitb
cgitb.enable()

import cgi
import os
form = cgi.FieldStorage()
loanNumber = form.getvalue("portfolio")
password = form.getvalue("password")
phase = form.getvalue("phase")


passkey = "python"
def getProfileTxid (loanNumber,phase):
  transaction=fetchMortgageProfileTxId(loanNumber,phase)
  if not transaction:
      return "False"
  else:
      return transaction 
def validateNumber (loanNumber):
  chainAddress=fetchMortgageAddress(loanNumber)
  if not chainAddress:
      return "False"
  else:
      return chainAddress
htmlContentType()
sessionTime="12:00:00"
uname="Portfolio"
divclassNavBar(uname,sessionTime)
divclassPageLocator("")
divclassOuterContainer()
print "<div id='chain' class='tableChain'>"

if not form:
	htmlHeader("Login Response")
    	print "<script language='Javascript'>"
	print "alert ('Loan number field is empty');"
	print "window.history.back();"
	print "</script>"
elif form.has_key("portfolio"):
    htmlHeader("Connected ...")
    print "<script language='Javascript'>"
    if not password:
	print "alert ('Please provide password');"
    elif password != passkey:
    	print "alert ('Incorrect Password');"
    print "window.history.back();"
    print "</script>"
    if (password==passkey):
      customerAddress=validateNumber(loanNumber)
      if (customerAddress == "False"):
        print "<script language='Javascript'>"
	print "alert ('Invalid Loan number');"
	print "window.history.back();"
        print "</script>"
      else:
        txid=getProfileTxid(loanNumber)
        if (txid == "False"):
            print "<script language='Javascript'>"
	    print "alert ('Invalid Loan number');"
	    print "window.history.back();"
            print "</script>"
        else:
            print "<script language='Javascript'>"
	    print "alert ('Loading customer portfolio');" 
            print "window.document.location.replace ('loanProfile.cgi?txid=%s');" % (txid)
            print "</script>"
print "</div>"
divEnd("outerContainer")
htmlFooter()
