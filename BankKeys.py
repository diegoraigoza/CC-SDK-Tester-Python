from Newtonsoft.Json import *
# 
# 
# example json file:
# 
# 
# 
# {
# 
# "publickey":"preston.CloudCoin.Global",
# 
# "privatekey":"6e2b96d6204a4212ae57ab84260e747f",
# 
# "email":""
# 
# }
# 
# 
class BankKeys(IKeys):
	def get_publickey(self):

	def set_publickey(self, value):

	publickey = property(fget=get_publickey, fset=set_publickey)

	def get_privatekey(self):

	def set_privatekey(self, value):

	privatekey = property(fget=get_privatekey, fset=set_privatekey)

	def get_email(self):

	def set_email(self, value):

	email = property(fget=get_email, fset=set_email)

	#Fields
	#Constructors
	def __init__(self, publickey=0, privatekey=0, email=0):
		self.publickey = publickey
		self.privatekey = privatekey
		self.email = email
    
  #end of constructor

	def __init__(self, publickey, privatekey, email):
		self.publickey = publickey
		self.privatekey = privatekey
		self.email = email
