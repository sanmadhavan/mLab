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
def displayChainList():
        print "<div id='chain' class='tableChainFull'>"
        print "<table class='table table-bordered'>"
        print "<thead class='defaultHeading'>"
        print "<tr>"
        print "        <th>Chain</th>"
        print "        <th>No of Blocks</th>"
        print "        <th>Transactions</th>"
        print "        <th>Addresses</th>"
        print "</tr>"
        print "</thead>"
        print"<tbody>"
        print "<tr>"
        print "<td class='undefined'><a href='/mortgage/mortgageChains.cgi'>Mortgage</a></td>"
        print "<td><a href='#'>%s</a></td>" % (str(1061))
        print "<td>%s</td>" % (str(15761))
        print "<td><a href='#'>%s</a></td>" % (str(261))
        print "</tr>"
        print "<tr>"
        print "<td class='undefined'><a href='#'>Private Banking</a></td>"
        print "<td><a href='#'>%s</a></td>" % (str(1022))
        print "<td>%s</td>" % (str(12323))
        print "<td><a href='#'>%s</a></td>" % (str(123))
        print "</tr>"
        print "<tr>"
        print "<td class='undefined'><a href='#'>Wealth</a></td>"
        print "<td><a href='#'>%s</a></td>" % (str(616))
        print "<td>%s</td>" % (str(13313))
        print "<td><a href='#'>%s</a></td>" % (str(131))
        print "</tr>"
        print "</table>"
        print "</div>"
# -----------------------------------------------------------------------------

def displaydashBoard():
        print "<div class='container-fluid'>"
        print "<div id='dashboard_target' width=100%></div>"

        print " <script type='text/javascript'>"
        print "         var db = new EmbeddedDashboard ();"
        print "         var chart2 = new ChartComponent();"
        print "         chart2.setDimensions (4, 4);"
        print "         chart2.setCaption('Chains');"
        print "         chart2.setLabels (['Mortgage', 'Private Banking', 'Wealth']);"
        print "         chart2.addSeries('transactions', 'Transactions', [15761, 12323, 13313]);"
        print "         db.addComponent (chart2);"
        print "         chart2.onItemClick (function (params) {"
        print "                 chart2.updateSeries ('series_1', [3, 5, 2]);"
        print "         });"
        print "         var chart21 = new ChartComponent();"
        print "         chart21.setDimensions (4, 4);"
        print "         chart21.setCaption('Amortization Type');"
        print "         chart21.setLabels (['Fixed','ARM']);"
        print "         chart21.setPieValues ([94,6], {"
        print "                  dataType: 'number',"
        print "                  numberSuffix: '%'"
        print "         });"
        print "         db.addComponent (chart21);"
        print "         db.embedTo('dashboard_target');"
        print "         var chart3 = new ChartComponent();"
        print "         chart3.setDimensions (4, 4);"
        print "         chart3.setCaption('Interest Rates');"
        print "         chart3.setLabels (['3.25','3.5', '3.65', '3.75','4.0','4.25']);"
        print "         chart3.setPieValues ([8,20,8,20,12,32], {"
        print "                  dataType: 'number',"
        print "                  numberSuffix: '%'"
        print "         });"
        print "         db.addComponent (chart3);"
        print "         db.embedTo('dashboard_target');"
        print "         var chart = new ChartComponent();"
        print "         chart.setDimensions (4, 4);"
        print "         chart.setCaption('Mortgage Type & Loan amount');    "
        print "         chart.setLabels (['Conventional', 'FHA', 'USDA','VA']);"
        print "         chart.addSeries ('loan', 'Loan Amount in $', [11531600, 145184653, 7476053,24675053]);"
        print "         db.addComponent (chart);"
        print "         var chart4 = new ChartComponent();"
        print "         chart4.setDimensions (4, 4);"
        print "         chart4.setCaption('Loan Amount %');"
        print "         chart4.setLabels (['Conventional', 'FHA', 'USDA', 'VA']);"
        print "         chart4.setPieValues ([8.15, 75.19, 3.88, 12.78], {"
        print "                  dataType: 'number',"
        print "                  numberSuffix: '%'"
        print "         });"
        print "         db.addComponent (chart4);"
        print "         db.embedTo('dashboard_target');"
        chart5=1
        if (chart5==1):
                print "            var chart5 = new ChartComponent();\
                        chart5.setDimensions (4, 4);\
                        chart5.setCaption('Account Distribution');\
                        chart5.setLabels (['California', 'Colorado', 'Florida','Georgia','Illinois','New Mexico','North Carolina','Oregon','Texas']);\
                        chart5.setPieValues ([23, 7,7,8,8,23,8,8,8], {\
                                dataType: 'number',\
                                numberSuffix: '%'\
                        });\
                        db.addComponent (chart5);       \
                        db.embedTo('dashboard_target');"
        print " </script>"
        print "</div>"



# -----------------------------------------------------------------------------
def showDashboardPage():
    sessionTime="12:00:00"
    uname="Guest"
    divclassNavBar(uname,sessionTime)
    divclassPageLocator("")
    divclassOuterContainer()
    displayChainList()
    displaydashBoard()
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







