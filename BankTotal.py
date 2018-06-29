from Newtonsoft.Json import *

class BankTotal(IBankResponse):
	def get_ones(self):

	def set_ones(self, value):

	ones = property(fget=get_ones, fset=set_ones)

	def get_fives(self):

	def set_fives(self, value):

	fives = property(fget=get_fives, fset=set_fives)

	def get_twentyfives(self):

	def set_twentyfives(self, value):

	twentyfives = property(fget=get_twentyfives, fset=set_twentyfives)

	def get_hundreds(self):

	def set_hundreds(self, value):

	hundreds = property(fget=get_hundreds, fset=set_hundreds)

	def get_twohundredfifties(self):

	def set_twohundredfifties(self, value):

	twohundredfifties = property(fget=get_twohundredfifties, fset=set_twohundredfifties)

	def get_bank_server(self):

	def set_bank_server(self, value):

	bank_server = property(fget=get_bank_server, fset=set_bank_server)

	def get_status(self):

	def set_status(self, value):

	status = property(fget=get_status, fset=set_status)

	def get_time(self):

	def set_time(self, value):

	time = property(fget=get_time, fset=set_time)

	#Fields
	#Constructors
	def __init__(self, ones=0, fives=0, twentyfives=0, hundreds=0, twohundredfifties=0):
		self.ones = ones
		self.fives = fives
		self.twentyfives = twentyfives
		self.hundreds = hundreds
		self.twohundredfifties = twohundredfifties

  #end of constructor

	def __init__(self, ones, fives, twentyfives, hundreds, twohundredfifties):
		self.ones = ones
		self.fives = fives
		self.twentyfives = twentyfives
		self.hundreds = hundreds
		self.twohundredfifties = twohundredfifties
