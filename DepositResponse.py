from Newtonsoft.Json import *

class DepositResponse(IBankResponse):
	def get_bank_server(self):

	def set_bank_server(self, value):

	bank_server = property(fget=get_bank_server, fset=set_bank_server)

	def get_time(self):

	def set_time(self, value):

	time = property(fget=get_time, fset=set_time)

	def get_status(self):

	def set_status(self, value):

	status = property(fget=get_status, fset=set_status)

	def get_message(self):

	def set_message(self, value):

	message = property(fget=get_message, fset=set_message)

	def get_receipt(self):

	def set_receipt(self, value):

	receipt = property(fget=get_receipt, fset=set_receipt)

	def get_account(self):

	def set_account(self, value):

	account = property(fget=get_account, fset=set_account)

	def __init__(self):
		pass
