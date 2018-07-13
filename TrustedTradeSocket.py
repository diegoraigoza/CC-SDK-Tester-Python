from System import *
from System.Collections.Generic import *
from System.Text import *
from System.Net.WebSockets import *
from System.Threading.Tasks import *
from Newtonsoft.Json import *
from System.Threading import *
from System.Linq import *

class TrustedTradeSocket(object):
	def __init__(self):
		self._status = Status.STATUS_DISCONNECTED
		self._errorMsg = ""

	class Status(object):
		def __init__(self):

	class PacketType(object):
		def __init__(self):

	def get_Url(self):

	Url = property(fget=get_Url)
