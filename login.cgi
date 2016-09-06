#!/usr/bin/python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
import sys
sys.path.append ('/opt/mchain/lib')
from mortgageHtmlElements import *
import mchainlog
logger = mchainlog.setup_custom_logger('root')
# -----------------------------------------------------------------------------
def loginForm():
    logger.info('Display login form')
    print "<body>"
    print "    <div class='loginBlock'>"
    print "        <div class='loginSection'>"
    print "            <center>"
    print "            <div class='brandLogo'>"
    print "                <img src='images/mphasis_logo.png' \
                                    class='brandLogoImage'/>"
    print "            </div>"
    print "            <div class='loginForm'>"
    print "                <form action='mortgage-landing.cgi' method='POST'>"
    print "                <input type='text' class='inputFields' \
                                    name='username' placeholder='Username' />"
    print "                <input type='password' class='inputFields' \
                                    name='password' placeholder='Password' />"
    print "                <button class='LoginFormButton' \
                                       id='loginSubmitButton'>LOG IN</button>"
    print "                <p>Forgot Password?</p>"
    print "            </div>"
    print "            </center>"
    print "        </div>"
    print "    </div>"
# -----------------------------------------------------------------------------


cgitb.enable()
htmlContentType()
htmlHeader("Mortgage mChain Login")
loginForm()
htmlFooter()
