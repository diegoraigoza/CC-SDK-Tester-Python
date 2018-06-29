from Newtonsoft.Json import *

class Receipt(IBankResponse):
	def get_receipt_id(self):

	def set_receipt_id(self, value):

	receipt_id = property(fget=get_receipt_id, fset=set_receipt_id)

	def get_time(self):

	def set_time(self, value):

	time = property(fget=get_time, fset=set_time)

	def get_timezone(self):

	def set_timezone(self, value):

	timezone = property(fget=get_timezone, fset=set_timezone)

	def get_bank_server(self):

	def set_bank_server(self, value):

	bank_server = property(fget=get_bank_server, fset=set_bank_server)

	def get_total_authentic(self):

	def set_total_authentic(self, value):

	total_authentic = property(fget=get_total_authentic, fset=set_total_authentic)

	def get_total_fracked(self):

	def set_total_fracked(self, value):

	total_fracked = property(fget=get_total_fracked, fset=set_total_fracked)

	def get_total_counterfeit(self):

	def set_total_counterfeit(self, value):

	total_counterfeit = property(fget=get_total_counterfeit, fset=set_total_counterfeit)

	def get_total_lost(self):

	def set_total_lost(self, value):

	total_lost = property(fget=get_total_lost, fset=set_total_lost)

	def get_rd(self):

	def set_rd(self, value):

	rd = property(fget=get_rd, fset=set_rd)
