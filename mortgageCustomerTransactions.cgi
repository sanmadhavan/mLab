#!/usr/bin/python
# -*- coding: UTF-8 -*-

# enable debugging
import sys
sys.path.append ('/opt/mchain/lib')
from mortgageHtmlElements import *
import mchainlog
logger = mchainlog.setup_custom_logger('root')

from mchainUtil import *
from mchainDB import *
from mchainLib import *

import cgitb
import cgi
from mortgageHtmlElements import *
cgitb.enable()

# ---------------------------------------------------------------------------------------
def displayBTransactions():
	addresses=[address,"dummy"]
	mbank={}
	mbank['name']=bankName
	mbank['address']=""
        customer=getMortgageCustomer(address)

        #print "<span class='alignLeft sideHeading'>Transaction History for %s [%s]</span>" %(customer['name'],address)
	print "<table class='table table-bordered'>"
        print "<thead class='defaultHeading'>"  
        print "<tr>"
        print "        <th>Customer Name</th>"
        print "        <th>Address</th>"
        print "        <th>Bank </th>"
        print "</tr>"
        print "</thead>"
	print "<tr>"
	#print "<td class='underlined'>%s</td>" %(btxid)
	print "<td>%s</td>" % (customer['name'])
	print "<td class='underlined'>%s</td>" % (customer['address'])
	print "<td>%s</td>" % (customer['bankname'])
	print "</tr>"
	print "</tbody>"
	print "</table>"

	print "<h2>Transaction History</h2>" 

	print "<table class='table table-bordered'>"
        print "<thead class='defaultHeading'>"  
        print "<tr>"
        print "        <th>Mortgage File</th>"
        print "        <th>Description</th>"
        print "        <th>Timestamp</th>"
        print "        <th>mchain Block</th>"
        print "</tr>"
        print "</thead>"
	print"<tbody>"
	testnet=False
	result = OP_RETURN_getChain_transactions(address, testnet)
	tlist=result['txns']
	tlist.reverse()

	for txns in tlist:
		txrow=txns.split('|')
		chistory = getmortgagechainTransaction (txrow[0],address)
			
        	print "<tr>"
                #print "<td class='underlined'>%s</td>" %(btxid)
		print "<td class='undefined'><a href='/mortgage/mortgageChainFile.cgi?txid=%s'>%s</a></td>" % (txrow[0],txrow[0])
                print "<td>%s</td>" % (chistory['description'])
                print "<td>%s</td>" % (chistory['timestamp'])
                print "<td>%s</td>" % (txrow[2])
        	print "</tr>"
        	print "</tbody>"
# ---------------------------------------------------------------------------------------


htmlContentType()
htmlHeader("Mortage Transactions")
form = cgi.FieldStorage()
address = (form.getvalue('address'))
bankName = (form.getvalue('bank'))
sessionTime="12:00:00"
uname="Guest"
divclassNavBar(uname,sessionTime)
divclassPageLocator("")
divclassOuterContainer()
	#place the table and contents here
print "<div id='chain' class='tableChain'>"

displayBTransactions()
print "</div>"
divEnd("outerContainer")
htmlFooter()

