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
from mortgageHtmlElements import *
cgitb.enable()

import cgi
import os
form = cgi.FieldStorage()
loanNumber = form.getvalue("loannumber")

passkey = "python"
def validateNumber (loanNumber):
  chainAddress=fetchMortgageAddress(loanNumber)
  if not chainAddress:
      return "False"
  else:
      return chainAddress
htmlContentType()
#print form.keys()
#print "text1 = "+str(text1)
#print "text2= "+ str(text2)

if not form:
	htmlHeader("Login Response")
    	print "<script language='Javascript'>"
	print "alert ('Loan number field is empty');"
	print "window.history.back();"
	print "</script>"
elif form.has_key("loannumber"):
    htmlHeader("Connected ...")
    customerAddress=validateNumber(loanNumber)
    if (customerAddress == "False"):
        print "<script language='Javascript'>"
	print "alert ('Invalid Loan number');"
	print "window.history.back();"
        print "</script>"
    else:
        #latestTxn=OP_RETURN_getLatestTxid(address,testnet)
        #latestTxn=OP_RETURN_getChain_transactions
        #print "<h1> txlatest=%s</h1>" % (latestTxn)

        print "<script language='Javascript'>"
        print "window.document.location.replace ('mortgageCustomerTransactions.cgi?address=%s')" % (customerAddress)
        print "</script>"
        
    htmlFooter()

else:
    htmlHeader("No success!")
    print "<script language='Javascript'>"
    if not password:
	print "alert ('Please provide password');"
    else:
    	print "alert ('Incorrect Password');"
    print "window.document.location.replace ('mchain-login.cgi');"
    print "</script>"
    
    print "<H3>Please go back and enter a valid login.</H3>"
htmlFooter()
