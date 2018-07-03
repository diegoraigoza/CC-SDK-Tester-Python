from System.Threading.Tasks import *

class ICloudBankAccessable(object):
	def LoadKeysFromFile(self, filepath):
		pass

	def get_CloudBankUtils(self):

	CloudBankUtils = property(fget=get_CloudBankUtils)

class ICloudBankUtils(object):
	def get_onesInBank(self):

	onesInBank = property(fget=get_onesInBank)

	def get_fivesInBank(self):

	fivesInBank = property(fget=get_fivesInBank)

	def get_twentyFivesInBank(self):

	twentyFivesInBank = property(fget=get_twentyFivesInBank)

	def get_hundredsInBank(self):

	hundredsInBank = property(fget=get_hundredsInBank)

	def get_twohundredfiftiesInBank(self):

	twohundredfiftiesInBank = property(fget=get_twohundredfiftiesInBank)

	def showCoins(self):
		pass

	def loadStackFromFile(self, filepath):
		pass

	def saveStackToFile(self, filepath):
		pass

	def getStackName(self):
		pass

	def sendStackToCloudBank(self):
		pass

	def getStackFromCloudBank(self, amountToWithdraw):
		pass

	def getReceipt(self):
		pass

	def getReceiptFromCloudBank(self):
		pass

	def transferCloudCoins(self, toPublicKey, coinsToSend):
		pass

class IKeys(object):
	def get_publickey(self):

	def set_publickey(self, value):

	publickey = property(fget=get_publickey, fset=set_publickey)

	def get_privatekey(self):

	def set_privatekey(self, value):

	privatekey = property(fget=get_privatekey, fset=set_privatekey)

	def get_account(self):

	def set_account(self, value):

	account = property(fget=get_account, fset=set_account)

class IBankResponse(object):
	def get_bank_server(self):

	def set_bank_server(self, value):

	bank_server = property(fget=get_bank_server, fset=set_bank_server)

	def get_time(self):

	def set_time(self, value):

	time = property(fget=get_time, fset=set_time)
