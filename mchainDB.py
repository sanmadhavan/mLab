import sqlite3

def fetchMSRProfileTxId (customername):
        conn = sqlite3.connect('/home/sanjeev/POC/data/mchain/mchainAccounts.db')
        c = conn.cursor()
        c.execute ("select profileTxid from MSRAccounts where customerName=?",(customername,))
        for row in c:
                return row[0]
def fetchInsuranceProfileTxId (customername):
        conn = sqlite3.connect('/home/sanjeev/POC/data/mchain/mchainAccounts.db')
        c = conn.cursor()
        c.execute ("select profileTxid from insuranceAccounts where customerName=?",(customername,))
        for row in c:
                return row[0]

def fetchMortgageProfileTxId (loanNumber,phase):
        conn = sqlite3.connect('/home/sanjeev/POC/data/mchain/mchainAccounts.db')
        c = conn.cursor()
        c.execute ("select profileTxid from mortgageAccounts where loanNumber=? and loanPhase=?",(loanNumber,phase,))
        for row in c:
                return row[0]
def fetchMSRCustomer (loanNumber):
        conn = sqlite3.connect('/home/sanjeev/POC/data/mchain/mchainAccounts.db')
        c = conn.cursor()
        c.execute ("select CustomerName from MSRAccounts where loanNumber=?",(loanNumber,))
        for row in c:
                return row[0]
def fetchMortgageCustomer (loanNumber):
        conn = sqlite3.connect('/home/sanjeev/POC/data/mchain/mchainAccounts.db')
        c = conn.cursor()
        c.execute ("select CustomerName from mortgageAccounts where loanNumber=?",(loanNumber,))
        for row in c:
                return row[0]
def fetchInsuranceCustomer (customername):
        conn = sqlite3.connect('/home/sanjeev/POC/data/mchain/mchainAccounts.db')
        c = conn.cursor()
        c.execute ("select mchainAddress from insuranceAccounts where CustomerName=?",(customername,))
        for row in c:
                return row[0]

def fetchMSRAddress (loanNumber):
        conn = sqlite3.connect('/home/sanjeev/POC/data/mchain/mchainAccounts.db')
        c = conn.cursor()
        c.execute ("select mchainAddress from MSRAccounts where loanNumber=?",(loanNumber,))
        for row in c:
                return row[0]
def fetchMortgageAddress (loanNumber):
        conn = sqlite3.connect('/home/sanjeev/POC/data/mchain/mchainAccounts.db')
        c = conn.cursor()
        c.execute ("select mchainAddress from mortgageAccounts where loanNumber=?",(loanNumber,))
        for row in c:
                return row[0]
def fetchInsuranceAddress (loanNumber):
        conn = sqlite3.connect('/home/sanjeev/POC/data/mchain/mchainAccounts.db')
        c = conn.cursor()
        c.execute ("select mchainAddress from insuranceAccounts where loanNumber=?",(loanNumber,))
        for row in c:
                return row[0]




def fetchInsuranceCompany(chainaddress):
        conn = sqlite3.connect('/home/sanjeev/POC/data/mchain/mchainAccounts.db')
        c = conn.cursor()
        c.execute ("select Name from mchainEntity where mchainAddress=?",(chainaddress,)) 
	for row in c:
		return row[0]

def getMSRCustomer(address):
        customer={}
        customer['name']=""
        customer['address']=""
        customer['bankname']=""
        conn = sqlite3.connect('/home/sanjeev/POC/data/mchain/mchainAccounts.db')
        c = conn.cursor()
        c.execute ("select BankName, CustomerName, mchainAddress from msrAccounts where mchainAddress=?",(address,)) 
	for row in c:
		customer['name']=row[1]
		customer['address']=row[2]
		customer['bankname']=row[0]
		continue
	return customer
def getInsuranceCustomer(address):
        customer={}
        customer['name']=""
        customer['address']=""
        customer['bankname']=""
        conn = sqlite3.connect('/home/sanjeev/POC/data/mchain/mchainAccounts.db')
        c = conn.cursor()
        c.execute ("select BankName, CustomerName, mchainAddress from InsuranceAccounts where mchainAddress=?",(address,)) 
	for row in c:
		customer['name']=row[1]
		customer['address']=row[2]
		customer['bankname']=row[0]
		continue
	return customer
def getMortgageCustomer(address):
        customer={}
        customer['name']=""
        customer['address']=""
        customer['bankname']=""
        conn = sqlite3.connect('/home/sanjeev/POC/data/mchain/mchainAccounts.db')
        c = conn.cursor()
        c.execute ("select BankName, CustomerName, mchainAddress from MortgageAccounts where mchainAddress=?",(address,)) 
	for row in c:
		customer['name']=row[1]
		customer['address']=row[2]
		customer['bankname']=row[0]
		continue
	return customer

def getCustomer(bankname,addresses):
        customer={}
        customer['name']=""
        customer['address']=""
        address1=addresses[0]
        address2=addresses[1]
        conn = sqlite3.connect('/home/sanjeev/POC/data/mchain/mchainAccounts.db')
        c = conn.cursor()
        if (bankname['name'] == "JPMC"):
                c.execute ("select name from JPMC_Accounts where address=?",(address1,)) 
                for row in c:
                        customer['name']=row[0]
                        customer['address']=address1
                        continue
                if (customer['name'] != ""): 
                        return customer
                else:
                        c.execute ("select name from JPMC_Accounts where address=?",(address2,)) 
                        for row in c:
                                customer['name']=row[0]
                                customer['address']=address2
                                continue
                        if (customer['name'] != ""): 
                                return customer
                        else:
                                return "--"
        else:
                c.execute ("select name from CITI_Accounts where address=?",(address1,)) 
                for row in c:
                        customer['name']=row[0]
                        customer['address']=address1
                        continue
                if (customer['name'] != ""): 
                        return customer
                else:
                        c.execute ("select name from CITI_Accounts where address=?",(address2,)) 
                        for row in c:
                                customer['name']=row[0]
                                customer['address']=address2
                                continue
                        if (customer['name']!=""):
                                return customer
        return customer

def getBankFromTransaction(addresses):
        bank={}
        bank['name']=""
        bank['address']=""
        address1=addresses[0]
        address2=addresses[1]
        conn = sqlite3.connect('/home/sanjeev/POC/data/mchain/mchainAccounts.db')
        c = conn.cursor()
        c.execute ("select Name from mchainEntity where mchainAddress=?",(address1,))
        for row in c:
                bank['name']=row[0]
                bank['address']=address1
                continue
        if (bank['name']!=""):
                return bank
        else:
                c.execute ("select Name from mchainEntity where mchainAddress =?",(address2,))
                for row in c:
                        bank['name']=row[0]
                        bank['address']=address2
                        continue
                if (bank['name']!=""):
                        return bank
                else:
                        bank['name']="--"
                        bank['address']=address2
        return bank
def getCustomerFromInsuranceTransaction(addresses):
        customer={}
        customer['name']=""
        customer['address']=""
        address1=addresses[0]
        address2=addresses[1]
        conn = sqlite3.connect('/home/sanjeev/POC/data/mchain/mchainAccounts.db')
        c = conn.cursor()
        c.execute ("select CustomerName from InsuranceAccounts where mchainAddress=?",(address1,))
        for row in c:
                customer['name']=row[0]
                customer['address']=address1
                continue
        if (customer['name']!=""):
                return customer
        else:
        	c.execute ("select CustomerName from InsuranceAccounts where mchainAddress=?",(address2,))
                for row in c:
                        customer['name']=row[0]
                        customer['address']=address2
                        continue
                if (customer['name']!=""):
                        return customer
                else:
                        customer['name']="--"
                        customer['address']=address2
        return customer
def getCustomerFromMortgageTransaction(addresses):
        customer={}
        customer['name']=""
        customer['address']=""
        address1=addresses[0]
        address2=addresses[1]
        conn = sqlite3.connect('/home/sanjeev/POC/data/mchain/mchainAccounts.db')
        c = conn.cursor()
        c.execute ("select CustomerName from MortgageAccounts where mchainAddress=?",(address1,))
        for row in c:
                customer['name']=row[0]
                customer['address']=address1
                continue
        if (customer['name']!=""):
                return customer
        else:
        	c.execute ("select CustomerName from MortgageAccounts where mchainAddress=?",(address2,))
                for row in c:
                        customer['name']=row[0]
                        customer['address']=address2
                        continue
                if (customer['name']!=""):
                        return customer
                else:
                        customer['name']="--"
                        customer['address']=address2
        return customer

def getCustomerFromMSRTransaction(addresses):
        customer={}
        customer['name']=""
        customer['address']=""
        address1=addresses[0]
        address2=addresses[1]
        conn = sqlite3.connect('/home/sanjeev/POC/data/mchain/mchainAccounts.db')
        c = conn.cursor()
        c.execute ("select CustomerName from MSRAccounts where mchainAddress=?",(address1,))
        for row in c:
                customer['name']=row[0]
                customer['address']=address1
                continue
        if (customer['name']!=""):
                return customer
        else:
        	c.execute ("select CustomerName from MSRAccounts where mchainAddress=?",(address2,))
                for row in c:
                        customer['name']=row[0]
                        customer['address']=address2
                        continue
                if (customer['name']!=""):
                        return customer
                else:
                        customer['name']="--"
                        customer['address']=address2
        return customer



def findBank(addresses):
        bank={}
        bank['name']=""
        bank['address']=""
        address1=addresses[0]
        address2=addresses[1]
        conn = sqlite3.connect('/home/sanjeev/POC/data/mchain/mchainAccounts.db')
        c = conn.cursor()
        c.execute ("select name from BankIds where address=?",(address1,))
        for row in c:
                bank['name']=row[0]
                bank['address']=address1
                continue
        if (bank['name']!=""):
                return bank
        else:
                c.execute ("select name from BankIds where address=?",(address2,))
                for row in c:
                        bank['name']=row[0]
                        bank['address']=address2
                        continue
                if (bank['name']!=""):
                        return bank
                else:
                        bank['name']="--"
                        bank['address']=address2
	return bank
def getInsuranceChainTransaction(txid,address):
	chistory={}
	chistory['address']=""
	chistory['desc']=""
	chistory['timestamp']=""
	conn = sqlite3.connect('/home/sanjeev/POC/data/mchain/mchainAccounts.db')
	c = conn.cursor()
	c.execute ("select CustomerAddress,Description,TimeStamp from insuranceCustomerHistory  where CustomerAddress=? and Txid=?",(address,txid))
	for row in c:
		chistory['address']=row[0]
		chistory['description']=row[1]
		chistory['timestamp']=row[2]
		continue
	return	chistory
def getmortgagechainTransaction(txid,address):
	chistory={}
	chistory['address']=""
	chistory['desc']=""
	chistory['timestamp']=""
	conn = sqlite3.connect('/home/sanjeev/POC/data/mchain/mchainAccounts.db')
	c = conn.cursor()
	c.execute ("select CustomerAddress,Description,TimeStamp from mortgageCustomerHistory  where CustomerAddress=? and Txid=?",(address,txid))
	for row in c:
		chistory['address']=row[0]
		chistory['description']=row[1]
		chistory['timestamp']=row[2]
		continue
	return	chistory

def getmsrchainTransaction(txid,address):
	chistory={}
	chistory['address']=""
	chistory['desc']=""
	chistory['timestamp']=""
	conn = sqlite3.connect('/home/sanjeev/POC/data/mchain/mchainAccounts.db')
	c = conn.cursor()
	c.execute ("select CustomerAddress,Description,TimeStamp from msrCustomerHistory  where CustomerAddress=? and Txid=?",(address,txid))
	for row in c:
		chistory['address']=row[0]
		chistory['description']=row[1]
		chistory['timestamp']=row[2]
		continue
	return	chistory


class DatabaseManager (object):
	def __init__(self,db):
		self.conn = sqlite3.connect(db)
		self.conn.execute('pragma foriegn_keys = on')
		self.conn.commit()
		self.cur = self.conn.cursor()
	def query(self,arg):
		print "arg = "
		print arg
		' '.join(arg)
		print "Joined"
		arg1 = str( arg)
		self.cur.execute(arg1)
		self.conn.commit()
		return self.cur

	def __del__(self):
		self.conn.close()
