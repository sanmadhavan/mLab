#!/usr/bin/python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
cgitb.enable()
import cgi
import sys
sys.path.append ('/opt/mchain/lib')
from mortgageHtmlElements import *
import mchainlog
from mchainUtil import *
from mchainDB import *
from mchainLib import *
from mortgageHtmlElements import *


# ---------------------------------------------------------------------------------------
def getBankName (address):
	conn = sqlite3.connect('/home/sanjeev/POC/data/mchain/mchainAccounts.db')
	c = conn.cursor()
	c.execute ("select name from BankIds where address=?",(address,))
	return c.fetchone()[0]



# ---------------------------------------------------------------------------------------
def displayTransactions(txid):
	#print "<div class='navHeading'>"
        #print "<span class='alignLeft sideHeading'>Transaction List</span>"
        #print "</div>"
	print "<table class='table table-bordered table-condensed'>"
	print "<thead class='defaultHeading'>"
	print "<tr>"
        print "        <td>Mortgage Files</td>"
        print "        <td>Financial Organisation</td>"
        print "        <td>Customer</td>"
        print "        <td>Customer Address</td>"
        print "        <td>Timestamp</td>"
	print "</tr>"
	print "</thead>"
	print"<tbody>"

	testnet=False
	result=OP_RETURN_get_transaction_data(txid,testnet)
	if 'error' in result:
		errString = result['error']['message']
	       	throwError(errString)
	txMetadata=(result['data'][0])
	mdata = binascii.unhexlify (txMetadata)
	lines = mdata.split('\n')
	lines.reverse()
        for line in lines:
		if line:
                	fields = line.split('|')
	                txid=fields[1]
			bankName=fields[2]
        	        bankerAddress=fields[3]
			customerName=fields[4]
        	        cAddress=fields[5]
        	        TimeStamp=fields[6]
			#bankName = getBankName (bankerAddress)
	                print "<tr>"
	                #print "<td class='underlined'>%s</td>" %(btxid)
	                print "<td class='undefined'><a href='/mortgage/mortgageChainFile.cgi?txid=%s'>%s</a></td>" % (txid,txid)
			print "<td style='border-right:1px solid #d3d3d3'>%s</td>" % (bankName)
			print "<td style='border-left:1px solid #d3d3d3; font-weight:bold'>%s</td>" % (customerName)
	                print "<td><a href='/mortgage/mortgageCustomerTransactions.cgi?address=%s'>%s</a></td>" % (cAddress,cAddress)
			print "<td style='border-right:1px solid #d3d3d3; font-weight:bold'>%s</td>" % (TimeStamp)
	                print "</tr>"
	                print "</tbody>"
	print "</table>"
        print "</div>"
# ---------------------------------------------------------------------------------------



	


htmlContentType()
htmlHeader("Mortgage Files")
form = cgi.FieldStorage()
txid = (form.getvalue('txid'))
sessionTime="12:00:00"
uname="Guest"
divclassNavBar(uname,sessionTime)
divclassPageLocator("mChain Transaction")
divclassOuterContainer()
	#place the table and contents here
print "<div id='chain' class='tableChain'>"
displayTransactions(txid)
print "</div>"
divEnd("outerContainer")
htmlFooter()

