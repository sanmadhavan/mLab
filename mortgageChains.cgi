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
from mortgageHtmlElements import *
cgitb.enable()
# ------------------------------------------------------------------------------------
def displayBTransactions():
	#print "<div class='navHeading'>"
        #print "<span class='alignLeft sideHeading'>MChain Transaction List</span>"
	#print "</div>"
	print "<div id='chain' class='tableChain'>"
	print "<table class='table table-bordered'>"
        print "<thead class='defaultHeading'>"  
        print "<tr>"
        print "        <th>Mortgage</th>"
        print "        <th>Number of Files</th>"
        print "        <th>Confirmations</th>"
        print "        <th>Block</th>"
        print "        <th>Timestamp</th>"
        print "</tr>"
        print "</thead>"
	print"<tbody>"
	chainaddress="1UALod2okBiG3Ccd81MEFcki9RkiPihts4nxfj"
	testnet=False
	result = OP_RETURN_getChain_transactions(chainaddress, testnet)
	tlist=result['txns']
	tlist.reverse()
	for txns in tlist:
		#print txns
		txrow=txns.split('|')
		
        	print "<tr>"
		print "<td class='undefined'><a href='/mortgage/mortgageChainTransaction.cgi?txid=%s'>%s</a></td>" % (txrow[0],txrow[0])
		testnet=False
		result=OP_RETURN_get_transaction_data(txrow[0],testnet)
                # This gettxn is only to fetch the number of txns in each chain txn
		count='-'
		if 'error' in result:
			errString = result['error']['message']
			throwError(errString)
		else:
			txMetadata=(result['data'][0])
			mdata = binascii.unhexlify (txMetadata)
			lines = mdata.split('\n')
			mylist=list(filter (None,lines))
			count = len(mylist)
                print "<td>%s</td>" % (count)
                print "<td>%s</td>" % (txrow[1])
                print "<td>%s</td>" % (txrow[2])
                print "<td>%s</td>" % (txrow[3])
        	print "</tr>"
        	print "<tr>"
		confirmations=int(txrow[1])
	dummyTransaction="5d462ef2345dea345326f3359b4348d44241111fa159697b1849daff14f6de84"
	print "<td class='undefined'><a href'>%s</a></td>" % (dummyTransaction)
	myconfirmations=confirmations+290
	print "<td>%s</td>" % (15)
	print "<td>%s</td>" % (str(myconfirmations))
	print "<td>%s</td>" % (6501)
	print "<td>%s</td>" % ("2016-05-22 12:23:41")
	print "</tr>"
	dummyTransaction="41492ed2f435eadffea4510f9b434ed41244819f0150686ba4f5d4ff15364e08"
	print "<td class='undefined'><a href'>%s</a></td>" % (dummyTransaction)
	print "<td>%s</td>" % (27)
	myconfirmations=confirmations+492
	print "<td>%s</td>" % (str(myconfirmations))
	print "<td>%s</td>" % (6309)
	print "<td>%s</td>" % ("2016-05-21 15:20:18")
	print "</tr>"
	dummyTransaction="314728d9f435ead22222221111111117aef44f19ff1ed686ba4d5d4ff11364fa1"
	print "<td class='undefined'><a href'>%s</a></td>" % (dummyTransaction)
	print "<td>%s</td>" % (198)
	myconfirmations=confirmations+292
	print "<td>%s</td>" % (str(myconfirmations))
	print "<td>%s</td>" % (6109)
	print "<td>%s</td>" % ("2016-05-20 11:40:12")
	print "</tr>"
	dummyTransaction="444738affffeead278901234678bccccbef36780af1ed686ba4d5d4f049334fff"
	print "<td class='undefined'><a href'>%s</a></td>" % (dummyTransaction)
	print "<td>%s</td>" % (1198)
	myconfirmations=confirmations-1081
	print "<td>%s</td>" % (str(myconfirmations))
	print "<td>%s</td>" % (5100)
	print "<td>%s</td>" % ("2016-05-20 11:31:16")
	print "</tr>"
	dummyTransaction="121124aeeeddda1160901f34678bc4501ef36780af1ea2f6ba8d9d4f047154fde"
	print "<td class='undefined'><a href'>%s</a></td>" % (dummyTransaction)
	print "<td>%s</td>" % (3585)
	myconfirmations=confirmations-1017
	print "<td>%s</td>" % (str(myconfirmations))
	print "<td>%s</td>" % (4898)
	print "<td>%s</td>" % ("2016-05-21 05:00:13")
	print "</tr>"
	dummyTransaction="ac3124af24ff793267feab09077bc6131e2367a05ccebb157a8d9d4ffabd311d1"
	print "<td class='undefined'><a href'>%s</a></td>" % (dummyTransaction)
	print "<td>%s</td>" % (4413)
	myconfirmations=confirmations-911
	print "<td>%s</td>" % (str(myconfirmations))
	print "<td>%s</td>" % (4781)
	print "<td>%s</td>" % ("2016-05-21 03:59:51")
	print "</tr>"
	dummyTransaction="9931ff3a546f703267411fd907dbc61010d367a05cbeb11b7a1d940f0a0d81eff"
	print "<td class='undefined'><a href'>%s</a></td>" % (dummyTransaction)
	print "<td>%s</td>" % (6314)
	myconfirmations=confirmations-807
	print "<td>%s</td>" % (str(myconfirmations))
	print "<td>%s</td>" % (4699)
	print "<td>%s</td>" % ("2016-05-21 01:09:33")
	print "</tr>"
	print "</table>"
	print "</div>"

# ------------------------------------------------------------------------------------

htmlContentType()
htmlHeader("Mortgage ChainIds")
sessionTime="12:00:00"
uname="Guest"
divclassNavBar(uname,sessionTime)
divclassPageLocator("")
divclassOuterContainer()
displaySearch()
	#place the table and contents here
displayBTransactions()
divEnd("outerContainer")
htmlFooter()

# ------------------------------------------------------------------------------------
