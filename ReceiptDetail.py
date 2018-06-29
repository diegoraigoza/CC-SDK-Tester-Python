from Newtonsoft.Json import *

class ReceiptDetail(object):
	def get_nn(self):

	def set_nn(self, value):

	nn = property(fget=get_nn, fset=set_nn)

	def get_sn(self):

	def set_sn(self, value):

	sn = property(fget=get_sn, fset=set_sn)

	def get_status(self):

	def set_status(self, value):

	status = property(fget=get_status, fset=set_status)

	def get_pown(self):

	def set_pown(self, value):

	pown = property(fget=get_pown, fset=set_pown)

	def get_note(self):

	def set_note(self, value):

	note = property(fget=get_note, fset=set_note)

	#Fields
	#Constructors
	def __init__(self, nn, sn, status, pown, note): #end of constructor
		self.nn = nn
		self.sn = sn
		self.status = status
		self.pown = pown
		self.note = note

	def __init__(self, nn, sn, status, pown, note):
		self.nn = nn
		self.sn = sn
		self.status = status
		self.pown = pown
		self.note = note
