#!/usr/bin/python
# -*- coding: UTF-8 -*-

# enable debugging
import xml.etree.ElementTree as ET
import cgi
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

# ---------------------------------------------------------------------------------------
def addPopup(doc):
	displayDoc="-"
	docname=""
	available="-"
	verified="-"
	timestamp="-"
	uploader="-"
	auditor="-"
	provider="-"
	complianceData={}
	for elt in doc:
		if (str(elt.tag) == "docname"):
			docname=str(elt.text)
		if (str(elt.tag) == "available"):
			available=str(elt.text)
		if (str(elt.tag) == "verified"):
			verified=str(elt.text)
		if (str(elt.tag) == "timestamp"):
			timestamp=str(elt.text)
		if (str(elt.tag) == "uploader"):
			uploader=str(elt.text)
		if (str(elt.tag) == "auditor"):
			auditor=str(elt.text)
		if (str(elt.tag) == "provider"):
			provider=str(elt.text)
		if (str(elt.tag) == "ComplianceCheck"):
			for compliance in elt:
				#complianceData.update(compliance.attrib.get('checklist'):compliance.attrib.get('value'))
				complianceData[compliance.attrib.get('checklist')]=compliance.attrib.get('value')
	if (docname ==""):
		return
					
	if (( available == "-") or (available == "NO")):
		print "<a title='Document Not available' style='color:red'> %s </a>" % (docname)
	else:
		print "<a data-toggle='modal' data-target='#%s'> %s </a>" % (docname.translate(None, string.punctuation + ' '),docname)

	print "	<div class='modal fade' id='%s' role='dialog' width = '50'>" % (docname.translate(None, string.punctuation + ' '))
	print "		<div class='modal-dialog modal-lg'>"
	print "			<div class='modal-content'>"
	print "				<div class='modal-header'>"
	print "					<h5 class='modal-title'>%s</h5>" % (docname)
	print "				</div>"
	print "				<div class='modal-body'>"
	print "					<div class='tableChainFull'>"
	print "						<table class='table table-borderless table-condensed'>"
	print "							<thead class='defaultHeading'>"
	print "							<tr>"
	print "								<td colspan='4'>Document Details</td>"
	print "							</tr>"
	print "							</thead>"
	print "							<tbody>"
	print	"							<tr>"
	print "								<td style='font-weight:bold'>Time Stamp</td>"
	print "								<td style='border-right:1px solid #d3d3d3'>%s</td>" % (timestamp)
	print "								<td style='font-weight:bold'>Uploaded By</td>"
	print "								<td>%s</td>" % (uploader)
	print "							</tr>"
	print "							<tr>"
	print "								<td style='font-weight:bold'>Availabilty</td>"
	print "								<td style='border-right:1px solid #d3d3d3'>%s</td>" % (available)
	print "								<td style='font-weight:bold'>Audited By</td>"
	print "								<td>%s</td>" % (auditor)
	print "							</tr>"
	print "							<tr>"
	print "								<td style='font-weight:bold'>Verification</td>"
	print "								<td style='border-right:1px solid #d3d3d3'>%s</td>" % (verified)
	print "								<td style='font-weight:bold'>Provided By</td>"
	print "								<td>%s</td>" % (provider)
	print "							</tr>"
	print "							</tbody>"
	print "						</table>"
	#=========== if complianceData
	if (complianceData):
		print "  				<table class='table table-borderless table-condensed'>"
		print "					<thead class='defaultHeading'>"
		print "					<tr>"
		print "						<td colspan='4'>Compliance Checks</td>"
		print "					</tr>"
		print "					</thead>"
		print "					<tbody>"
		for key, value in complianceData.iteritems():
			print "				<tr>"
			print "					<td>%s</td>" % (key)
			print "					<td>%s</td>" %(value)
			print "				</tr>"
		print "					</tbody>"
		print "				</table>"
		print "  				<table class='table table-borderless table-condensed'>"
		print "					<thead class='defaultHeading'>"
		print "					<tr>"
		print "						<td colspan='4'>Policy Document</td>"
		print "					</tr>"
		print "					</thead>"
		print "				   </table>"
		print "				<div class='container-fluid'>"
		print "					<object style='align:center;'><embed width='700px' height='auto' src='customer/samplepolicy.pdf' type='application/pdf'></object>"
		print "				</div>"
	#=========== if complianceData
	print "					</div>"
	print "				</div>"
	print "<div class='modal-footer'>"
	print "<button type='button' class='btn btn-default' data-dismiss='modal'>Close</button>"
	print "</div>"
	print "			</div>"
	print "		</div>"
	print "	</div>"
	print "<a>|</a>"
# ---------------------------------------------------------------------------------------

def displayBorrowerProfile(child):
			print "<table class='table table-borderless table-condensed'>"
			print "<thead class='defaultHeading'>"
			print "<tr>"
			print "<td colspan='6'>Borrower Profile</td>"
			print "</tr>"
			print "</thead>"
			print"<tbody>"
			borrower="-"
			borrowertype="-"
			ltvratio="-"
			loannumber="-"
			ssn="-"
			appraisal="-"
			for fdata in child:
				if (str(fdata.tag) == "Borrower"):
					borrower=str(fdata.text)
				if (str(fdata.tag) == "BorrowerType"):
					borrowertype=str(fdata.text)
				if (str(fdata.tag) == "TVratio"):
					ltvratio=str(fdata.text)
				if (str(fdata.tag) == "LoanNumber"):
					loannumber=str(fdata.text)
				if (str(fdata.tag) == "SSN"):
					ssn=str(fdata.text)
				if (str(fdata.tag) == "Appraisal"):
					appraisal=str(fdata.text)
			print "<tbody>"
			print "<tr>"
			print "<td style='font-weight:bold'>Name</td>"
			print "<td style='border-right:1px solid #d3d3d3'>%s</td>" % (borrower)
			print "<td style='font-weight:bold'>Type</td>"
			print "<td>%s</td>" %(borrowertype)
			print "<td style='border-left:1px solid #d3d3d3; font-weight:bold'>LTV Ratio</td>"
			print "<td>%s</td>" % (ltvratio)
			print "</tr>"
			print "<tr>"
			print "<td style='font-weight:bold'>Loan Number</td>"
			print "<td style='border-right:1px solid #d3d3d3'>%s</td>" % (loannumber)
			print "<td style='font-weight:bold'>SSN No.</td>"
			print "<td>%s</td>" % (ssn)
			print "<td style='border-left:1px solid #d3d3d3; font-weight:bold'>APR</td>"
			print "<td>%s</td>" % (appraisal)
			print "</tr>"
			print "</tbody>"
			print "</table>"
#===============================================================================================
def getloanNumber(child):
			borrower="-"
			borrowertype="-"
			ltvratio="-"
			loannumber="-"
			ssn="-"
			appraisal="-"
			for fdata in child:
				if (str(fdata.tag) == "Borrower"):
					borrower=str(fdata.text)
				if (str(fdata.tag) == "BorrowerType"):
					borrowertype=str(fdata.text)
				if (str(fdata.tag) == "TVratio"):
					ltvratio=str(fdata.text)
				if (str(fdata.tag) == "LoanNumber"):
					loannumber=str(fdata.text)
					return loannumber
				if (str(fdata.tag) == "SSN"):
					ssn=str(fdata.text)
				if (str(fdata.tag) == "Appraisal"):
					appraisal=str(fdata.text)
			return 0
#===============================================================================================
#===============================================================================================
def getInsuranceStatus(child):
			mortgageType="-"
			amortizationType="-"
			loanAmount="-"
			loanTerm="-"
			interestRate="-"
			loanStatus="-"
			insuranceStatus="-"
			for fdata in child:
				if (str(fdata.tag) == "mortgageType"):
					mortgageType=str(fdata.text)
				if (str(fdata.tag) == "amortizationType"):
					amortizationType=str(fdata.text)
				if (str(fdata.tag) == "loanAmount"):
					loanAmount=str(fdata.text)
				if (str(fdata.tag) == "loanterm"):
					loanTerm=str(fdata.text)
				if (str(fdata.tag) == "interestRate"):
					interestRate=str(fdata.text)
				if (str(fdata.tag) == "loanStatus"):
					loanStatus=str(fdata.text)
				if (str(fdata.tag) == "insurance"):
					insuranceStatus=str(fdata.text)
			if (insuranceStatus == "Pending"):
				return 1
			elif (insuranceStatus == "Received"):
				return 1
			else:
				return 0
#===============================================================================================
def displayMortgageInfo(child):
			print "<table class='table table-borderless table-condensed'>"
			print "<thead class='defaultHeading'>"
			print "<tr>"
			print "<td colspan='8'>Mortgage Information</td>"
			print "</tr>"
			print "</thead>"
			print"<tbody>"
			mortgageType="-"
			amortizationType="-"
			loanAmount="-"
			loanTerm="-"
			interestRate="-"
			loanStatus="-"
			insuranceStatus="-"
			for fdata in child:
				if (str(fdata.tag) == "mortgageType"):
					mortgageType=str(fdata.text)
				if (str(fdata.tag) == "amortizationType"):
					amortizationType=str(fdata.text)
				if (str(fdata.tag) == "loanAmount"):
					loanAmount=str(fdata.text)
				if (str(fdata.tag) == "loanterm"):
					loanTerm=str(fdata.text)
				if (str(fdata.tag) == "interestRate"):
					interestRate=str(fdata.text)
				if (str(fdata.tag) == "loanStatus"):
					loanStatus=str(fdata.text)
				if (str(fdata.tag) == "insurance"):
					insuranceStatus=str(fdata.text)
			print "<tbody>"
			print "<tr>"
			print "<td style='font-weight:bold'>Mortgage Type</td>"
			print "<td style='border-right:1px solid #d3d3d3'>%s</td>" % (mortgageType)
			print "<td style='font-weight:bold'>Amortization Type</td>"
			print "<td>%s</td>" %(amortizationType)
			print "<td style='border-left:1px solid #d3d3d3; font-weight:bold'>Loan Amount</td>"
			print "<td>%s</td>" % (loanAmount)
			print "<td style='border-left:1px solid #d3d3d3; font-weight:bold'>Term</td>"
			print "<td>%s</td>" % (loanTerm)
			print "</tr>"
			print "<tr>"
			print "<td style='font-weight:bold'>Interest Rate</td>"
			print "<td style='border-right:1px solid #d3d3d3'>%s</td>" % (interestRate)
			print "<td style='font-weight:bold'>Loan Status</td>"
			if ((loanStatus == "Approved") or (loanStatus == "Disbursed")):
				print "<td><a style='color:green'>%s </a></td>" % (loanStatus)
			else:
				print "<td>%s</td>" % (loanStatus)
			print "<td style='border-left:1px solid #d3d3d3; font-weight:bold'>Insurance</td>"
			if (insuranceStatus == "Pending"):
				print "<td><a title='Loan not disbursed without Insurance' style='color:red'>%s</a></td>" % (insuranceStatus)
			elif (insuranceStatus == "Received"):
				print "<td><a style='color:green'>%s</a></td>" % (insuranceStatus)
			else:
				print "<td>%s</td>" % (insuranceStatus)
			print "<td style='border-left:1px solid #d3d3d3; font-weight:bold'></td>"
			print "<td></td>" 
			print "</tr>"
			print "</tbody>"
			print "</table>"
#===============================================================================================
def displayPropertyInfo(child):
			print "<table class='table table-borderless table-condensed'>"
			print "<thead class='defaultHeading'>"
			print "<tr>"
			print "<td colspan='6'>Property Information</td>"
			print "</tr>"
			print "</thead>"
			print"<tbody>"
			purpose="-"
			propertyType="-"
			initialDeposit="-"
			Address="-"
			floodZone="-"
			emi="-"
			for fdata in child:
				if (str(fdata.tag) == "purpose"):
					purpose=str(fdata.text)
				if (str(fdata.tag) == "propertyType"):
					propertyType=str(fdata.text)
				if (str(fdata.tag) == "initialDeposit"):
					initialDeposit=str(fdata.text)
				if (str(fdata.tag) == "Address"):
					Address=str(fdata.text)
				if (str(fdata.tag) == "floodZone"):
					floodZone=str(fdata.text)
				if (str(fdata.tag) == "emi"):
					emi=str(fdata.text)
			print "<tbody>"
			print "<tr>"
			print "<td style='font-weight:bold'>Property Type</td>"
			print "<td>%s</td>" %(propertyType)
			print "<td style='border-left:1px solid #d3d3d3; font-weight:bold'>Address</td>"
			print "<td>%s</td>" % (Address)
			print "</tr>"
			print "<tr>"
			print "<td style='font-weight:bold'>Purpose</td>"
			print "<td style='border-right:1px solid #d3d3d3'>%s</td>" % (purpose)
			print "<td style='border-left:1px solid #d3d3d3; font-weight:bold'>Initial Deposit</td>"
			print "<td>%s</td>" % (initialDeposit)
			print "</tr>"
			print "<tr>"
			print "<td style='font-weight:bold'>Flood Zone</td>"
			print "<td style='border-right:1px solid #d3d3d3'>%s</td>" % (floodZone)
			print "<td style='font-weight:bold'>EMI</td>"
			print "<td>%s</td>" % (emi)
			print "</tr>"
			print "</tbody>"
			print "</table>"
#===============================================================================================



def displayLoanData():
        testnet=False
        result=OP_RETURN_get_transaction_data(txid,testnet)
        #print result
        if 'error' in result:
                errString = result['error']['message']
                throwError(errString)
        blockhash=str(result['blockhash'])
        block=OP_RETURN_bitcoin_cmd('getblock', testnet,blockhash)
        if 'error' in block:
                errString = result['error']['message']
                throwError(errString)
        blockNumber=block['height']
        confirmations=result['confirmations']
        dateTime=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(result['time']))
        print "<h2>Blockchain Information</h2>"

        print "<table class='table table-bordered'>"
        print "<thead class='defaultHeading'>"
        print "<tr>"
        print "        <td>Block Address</td>"
        print "        <td>Block</td>"
        print "        <td>Confirmations</td>"
        print "        <td>Timestamp</td>"
        print "</tr>"
        print "</thead>"
        print"<tbody>"
        print "<tr>"
        print "        <td>%s</td>" % (blockhash)
        print "        <td> %s </td>" % (blockNumber)
        print "        <td> %s </td>" % (confirmations)
        print "        <td>%s</td>" % (str(dateTime))
        print "</tr>"
        print "</table>"
        print "<table class='table table-bordered'>"
        print "<thead class='defaultHeading'>"
        print "<tr>"
        print "        <td>Financial Organisation</td>"
        print "        <td>Address</td>"
        print "        <td>Customer</td>"
        print "        <td>Customer Address</td>"
        print "</tr>"
        print "</thead>"
        bank={}
        bank['name']="undefined"
        bank['address']=""
        bank=getBankFromTransaction(result['myaddresses'])
        customer={}
        customer['name']=""
        customer['address']=""
        customer= getCustomerFromMortgageTransaction(result['myaddresses'])

        print"<tbody>"
        print "<tr>"
        print "        <td class='underlined' >%s</td>" % (bank['name'])
        print "        <td class='underlined'>%s</td>" % (bank['address'])
        print "        <td class='underlined'> %s </td>" % (customer['name'])
        print "        <td class='undefined'><a href='/mortgage/mortgageCustomerTransactions.cgi?address=%s'>%s</a></td>" %(customer['address'],customer['address'])
        print "</tr>"
        print "</tbody>"
        print "</table>"
        txMetadata=(result['data'][0])
        mdata = binascii.unhexlify (txMetadata)

        loanfile="/opt/mchain/cgi/data/"+txid+".xml"
        f=open(loanfile,"w")
        f.write(mdata)
        f.close()
        loanfile="/opt/mchain/cgi/data/payments.xml"
        tree = ET.parse(loanfile)
        root = tree.getroot()


	iStatus=0
	for child in root:
		if (child.tag == "BorrowerProfile"):
			loanNum=getloanNumber(child)
		if (child.tag == "MortgageInfo"):
			iStatus=getInsuranceStatus(child)
	if (iStatus==1):
        	print "<h2>Portfolio&nbsp&nbsp<span style='font-size:15px;'>To share this file, <a href='/mortgage/viewPortfolio.cgi?loannumber=%s' target='popup' onclick=\"window.open('/mortgage/viewPortfolio.cgi?loannumber=%s','Portfolio','width=1400,height=800')\" >cick here</a></span></h2>" % (loanNum,loanNum)
	else:
        	print "<h2>Portfolio</h2>"

	for child in root:
		#===========================================================================================
		if (child.tag == "BorrowerProfile"):
			displayBorrowerProfile(child)
		if (child.tag == "MortgageInfo"):
			displayMortgageInfo(child)
		if (child.tag == "PropertyInfo"):
			displayPropertyInfo(child)
			#pass


	for child in root:
		if (child.tag == "Documents"):
			print "<table class='table table-borderless table-condensed'>"
			print "<thead class='defaultHeading'>"
			print "<tr>"
			print "<td colspan='6'>Documents</td>"
			print "</tr>"
			print "</thead>"
			for fdata in child:
				print "<tr>"
				print "<td colspan='6' style='font-weight:bold'>%s</td>" % (str(fdata.attrib.get('display')))
				print "</tr>"
				print "<td style='border-right:1px solid #d3d3d3'>"
				for doc in fdata:
					addPopup(doc)
		        print "<tr>"
			print "<td colspan='6' style='font-weight:bold'> </td>"  # Added this to insert a blank space before payments.
			print "</tr>"

        paymentfile="/opt/mchain/cgi/data/payments.xml"
        tree1 = ET.parse(paymentfile)
        root1 = tree1.getroot()
        for child in root1:
           if (child.tag == "Payments"):
              print "<thead class='defaultHeading'>"
              print "<tr><td colspan='6'>Payments</td></tr>"
              print "</thead>"
              print"<tbody>"
              print "<tr><td>"
              print "<div class='container-fluid'><!--Accordion Start-->"
              print "  <div class='panel-group col-lg-12 col-md-12 well ' id='accordion'>"
              emitimestamp="-"
              emidesc="-"
              emitxnref="-"
              emitxnmethod="-"
              emiamount="-"
              emistatus="-"
              emiloan_OS="-"
              for fdata in child:
                 myyear=str(fdata.attrib.get('display'))
                 print "    <div class='panel panel-default'><!--2003-->" 
                 print "      <div class='panel-heading'>"
                 print "          <h4 class='panel-title'>"
                 print "              <a data-toggle='collapse' data-parent='#accordion' href=\"#%s\">%s</a>" %(myyear,myyear)
                 print "          </h4>"
                 print "      </div>"
                 print "      <div id='%s' class='panel-collapse collapse'>" % (myyear)
                 print "         <div class='panel-body'><!--inner acc start-->"
                 for emiMonth in fdata:
                     displayMon = str(emiMonth.attrib.get('month'))
                     hrefTag = myyear+"_"+displayMon
                     print "         <div class='panel panel-default'><!--jan-->"
                     print "            <div class='panel-heading'>"
                     print "               <h4 class='panel-title'>"
                     print "                  <a data-toggle='collapse' data-parent=\"#%s\" href=\"#%s\">%s</a>" %(myyear,hrefTag,displayMon)
                     print "               </h4>"
                     print "            </div>"
                     print "            <div id=\"%s\" class='panel-collapse collapse'>" % (hrefTag)
                     print "                <div class='panel-body'>"
                     print "                   <table class='table table-bordered'>"
                     print "                   <thead  class='defaultHeading'>"
                     print "                      <tr><td>TimeStamp</td><td>Description</td><td>Transaction Ref</td><td>Method</td><td>Amount</td><td>Status</td><td>O/S Amount</td></tr>"
                     print "                   </thead><tbody>"
                     for txnData in emiMonth:
                         if (str(txnData.tag) == "timestamp"):
                             emitimestamp=str(txnData.text)
                         if (str(txnData.tag) == "description"):
                             emidesc=str(txnData.text)
                         if (str(txnData.tag) == "txnref"):
                             emitxnref=str(txnData.text)
                         if (str(txnData.tag) == "method"):
                             emitxnmethod=str(txnData.text)
                         if (str(txnData.tag) == "amount"):
                             emiamount=str(txnData.text)
                         if (str(txnData.tag) == "status"):
                             emistatus=str(txnData.text)
                         if (str(txnData.tag) == "outstanding"):
                             emiloan_OS=str(txnData.text)

                     print "                   <tr><!--the empty row starts here-->"
                     print "                      <td>%s</td>" % (emitimestamp)
                     print "                      <td>%s</td>" % (emidesc)
                     print "                      <td>%s</td>" % (emitxnref)
                     print "                      <td>%s</td>" % (emitxnmethod)
                     print "                      <td>%s</td>" % (emiamount)
                     print "                      <td>%s</td>" % (emistatus)
                     print "                      <td>%s</td>" % (emiloan_OS)
                     print "                   </tr><!--empty row ends here-->"
                     print "                   </tbody>"
                     print "                   </table><!--the inner table ends here-->"
                     print "                </div>"
                     print "             </div>"
                     print "         </div><!--jan ends-->"
                 print "         </div>"
                 print "     </div>"
                 print "     </div><!--2003 ends-->"
              print "     </div>"
              print "</div>"
              print "</td></tr></tbody></table>"

# ---------------------------------------------------------------------------------------

htmlContentType()
htmlHeader("Mortgage File")
cgitb.enable()
form = cgi.FieldStorage()
txid = (form.getvalue('txid'))
if not txid:
  sessionTime="12:00:00"
  uname="Guest"
  divclassNavBar(uname,sessionTime)
  print "<script language='Javascript'>"
  print "alert ('invalid transaction id');"
  print "window.history.back();"
  print "</script>"
  htmlFooter()

sessionTime="12:00:00"
uname="Guest"
divclassNavBar(uname,sessionTime)
divclassPageLocator("")
divclassOuterContainer()
print "<div id='chain' class='tableChain'>"
displayLoanData()
print "</div>"
divEnd("outerContainer")
htmlFooter()

