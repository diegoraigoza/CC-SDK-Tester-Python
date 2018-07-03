from Newtonsoft.Json import *
# 
# example json file:
# 
# {
# "publickey":"preston.CloudCoin.Global",
# "privatekey":"6e2b96d6204a4212ae57ab84260e747f",
# "email":""
# }
# 
class BankKeys(IKeys):
	def get_publickey(self):

	def set_publickey(self, value):

	publickey = property(fget=get_publickey, fset=set_publickey)

	def get_privatekey(self):

	def set_privatekey(self, value):

	privatekey = property(fget=get_privatekey, fset=set_privatekey)

	def get_account(self):

	def set_account(self, value):

	account = property(fget=get_account, fset=set_account)

	#Fields
	#Constructors
	def __init__(self, publickey, privatekey, account): #end of constructor
		self.publickey = publickey
		self.privatekey = privatekey
		self.account = account

	def __init__(self, publickey, privatekey, account):
		self.publickey = publickey
		self.privatekey = privatekey
		self.account = account
