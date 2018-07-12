from System.Collections.Generic import *
from System.IO import *
from System import *
from System.Net.Http import *
from System.Threading.Tasks import *
from Newtonsoft.Json import *

class CloudBankUtils(ICloudBankUtils):
	#Fields
	def get_onesInBank(self):

	def set_onesInBank(self, value):

	onesInBank = property(fget=get_onesInBank, fset=set_onesInBank)

	def get_fivesInBank(self):

	def set_fivesInBank(self, value):

	fivesInBank = property(fget=get_fivesInBank, fset=set_fivesInBank)

	def get_twentyFivesInBank(self):

	def set_twentyFivesInBank(self, value):

	twentyFivesInBank = property(fget=get_twentyFivesInBank, fset=set_twentyFivesInBank)

	def get_hundredsInBank(self):

	def set_hundredsInBank(self, value):

	hundredsInBank = property(fget=get_hundredsInBank, fset=set_hundredsInBank)

	def get_twohundredfiftiesInBank(self):

	def set_twohundredfiftiesInBank(self, value):

	twohundredfiftiesInBank = property(fget=get_twohundredfiftiesInBank, fset=set_twohundredfiftiesInBank)

	#Constructor
	def __init__(self, startKeys):
		self._keys = startKeys
		self._cli = HttpClient()
		self._totalCoinsWithdrawn = 0
		self.onesInBank = 0
		self.fivesInBank = 0
		self.twentyFivesInBank = 0
		self.hundredsInBank = 0
		self.twohundredfiftiesInBank = 0
 #end constructor
	#Methods
	#The results are saved in this class's public properties if successful.
	def showCoins(self):
		"""<summary>Calls the CloudService's show_coins service for the server that this object holds the keys for.</summary>"""
		#the private key is sent as form url encoded content
		#var formContent = new FormUrlEncodedContent(new[] { new KeyValuePair<string, string>("pk", keys.privatekey), new KeyValuePair<string, string>("account", keys.account) });
		json = "error"
		try:
			showCoins = self._cli.GetAsync("https://" + self._keys.publickey + "/show_coins.aspx?pk=" + self._keys.privatekey + "&account=" + self._keys.account)
			json = showCoins.Content.ReadAsStringAsync()
			bankTotals = JsonConvert.DeserializeObject(json)
			if bankTotals.status == "coins_shown":
				self.onesInBank = bankTotals.ones
				self.fivesInBank = bankTotals.fives
				self.twentyFivesInBank = bankTotals.twentyfives
				self.hundredsInBank = bankTotals.hundreds
				self.twohundredfiftiesInBank = bankTotals.twohundredfifties
			else:
				Console.Out.WriteLine(bankTotals.status)
				failResponse = JsonConvert.DeserializeObject(json)
				Console.Out.WriteLine(failResponse.message)
		except HttpRequestException, ex:
			Console.Out.WriteLine("Exception: " + ex.Message)
			Console.Out.WriteLine("Check your connection, or your public key")
			return 
		except JsonSerializationException, ex: #end try catch
			Console.Out.WriteLine(ex.Message)
			Console.Out.WriteLine(json)
		except JsonReaderException, ex:
			Console.Out.WriteLine(ex.Message)
			Console.Out.WriteLine(json)
		finally:
 #end show coins
	def loadStackFromFile(self, filepath):
		"""<summary>Sets rawStackForDeposit to a CloudCoin stack read from a file</summary>
		<param name="filepath">The full filepath and filename of the CloudCoin stack that is being loaded</param> 
		"""
		self._rawStackForDeposit = File.ReadAllText(filepath)

	#loadStackFromFile needs to be called first
	def sendStackToCloudBank(self):
		"""<summary>Sends the CloudCoin in rawStackForDeposit to the CloudService server that this object holds the keys for</summary>"""
		CloudBankFeedback = ""
		formContent = FormUrlEncodedContent(Array[]((KeyValuePair[str, str]("stack", self._rawStackForDeposit), KeyValuePair[str, str]("account", self._keys.account))))
		try:
			result_stack = self._cli.PostAsync("https://" + self._keys.publickey + "/deposit_one_stack.aspx", formContent)
			CloudBankFeedback = result_stack.Content.ReadAsStringAsync()
			cbf = JsonConvert.DeserializeObject(CloudBankFeedback)
			Console.Out.WriteLine(cbf.message)
			self._receiptNumber = cbf.receipt
		except HttpRequestException, ex:
			Console.Out.WriteLine("Exception: " + ex.Message)
			Console.Out.WriteLine("Check your connection, or your public key")
			return 
		except JsonSerializationException, ex:
			Console.Out.WriteLine(ex.Message)
			Console.Out.WriteLine(CloudBankFeedback)
		except JsonReaderException, ex:
			Console.Out.WriteLine(ex.Message)
			Console.Out.WriteLine(CloudBankFeedback)
		finally:
 #End send stack
	#loadStackFromFile needs to be called first
	def sendStackToCloudBank(self, toPublicURL):
		"""<summary>Sends the CloudCoin in rawStackForDeposit to a CloudService server specified by parameter <paramref name="toPublicURL"/></summary>
		<param name="toPublicURL">The url of the CloudService server the CloudCoins are being sent to. Do not include "https://"</param>
		"""
		CloudBankFeedback = ""
		formContent = FormUrlEncodedContent(Array[]((KeyValuePair[str, str]("stack", self._rawStackForDeposit), KeyValuePair[str, str]("account", self._keys.account))))
		try:
			result_stack = self._cli.PostAsync("https://" + toPublicURL + "/deposit_one_stack.aspx", formContent)
			CloudBankFeedback = result_stack.Content.ReadAsStringAsync()
			cbf = JsonConvert.DeserializeObject(CloudBankFeedback)
			Console.Out.WriteLine(cbf.message)
			self._receiptNumber = cbf.receipt
		except HttpRequestException, ex:
			Console.Out.WriteLine("Exception: " + ex.Message)
			Console.Out.WriteLine("Check your connection, or your public key")
			return 
		except JsonSerializationException, ex:
			Console.Out.WriteLine(ex.Message)
			Console.Out.WriteLine(CloudBankFeedback)
		except JsonReaderException, ex:
			Console.Out.WriteLine(ex.Message)
			Console.Out.WriteLine(CloudBankFeedback)
		finally:
 #End send stack
	#Requires sendStackToCloudBank to have been previously called
	#The retrieved receipt will be saved in rawReceipt
	def getReceipt(self):
		"""<summary>Retrieve the receipt generated by the CloudService for the last sendStackToCloudBank call</summary>"""
		try:
			result_receipt = self._cli.GetAsync("https://" + self._keys.publickey + "/get_receipt.aspx?rn=" + self._receiptNumber + "&account=" + self._keys.account)
			self._rawReceipt = result_receipt.Content.ReadAsStringAsync()
		except HttpRequestException, ex:
			Console.Out.WriteLine("Exception: " + ex.Message)
			Console.Out.WriteLine("Check your connection, your public key, or you may not have made a Deposit yet.")
			return 
		finally:
 #End get Receipt
	#The resulting stack that is retrieved is saved in rawStackFromWithdrawal
	def getStackFromCloudBank(self, amountToWithdraw):
		"""<summary>Retrieves CloudCoins from CloudService server that this object holds the keys for.</summary>
		<param name="amountToWithdraw">The amount of CloudCoins to withdraw</param>
		"""
		self._totalCoinsWithdrawn = amountToWithdraw
		#var formContent = new FormUrlEncodedContent(new[] { new KeyValuePair<string,string>("amount",amountToWithdraw.ToString()),
		#   new KeyValuePair<string, string>("pk", keys.privatekey), new KeyValuePair<string, string>("account", keys.account) });
		try:
			result_stack = self._cli.GetAsync("https://" + self._keys.publickey + "/withdraw_one_stack.aspx?pk=" + self._keys.privatekey + "&amount=" + amountToWithdraw + "&account" + self._keys.account)
			self._rawStackFromWithdrawal = result_stack.Content.ReadAsStringAsync()
			failResponse = JsonConvert.DeserializeObject(self._rawStackFromWithdrawal)
			Console.Out.WriteLine(failResponse.status)
			Console.Out.WriteLine(failResponse.message)
		except HttpRequestException, ex:
			Console.Out.WriteLine("Exception: " + ex.Message)
			Console.Out.WriteLine("Check your connection, or your public key")
			return 
		except JsonReaderException, ex:
			Console.Out.WriteLine(self._rawStackFromWithdrawal)
		except JsonSerializationException, ex:
			Console.Out.WriteLine(self._rawStackFromWithdrawal)
		finally:
 #End get stack from cloudbank
	def getDenomination(self, sn):
		"""<summary>Calculate a CloudCoin note's denomination using it serial number(sn)</summary>"""
		nom = 0
		if (sn < 1):
			nom = 0
		elif (sn < 2097153):
			nom = 1
		elif (sn < 4194305):
			nom = 5
		elif (sn < 6291457):
			nom = 25
		elif (sn < 14680065):
			nom = 100
		elif (sn < 16777217):
			nom = 250
		else:
			nom = '0'
		return nom
 #end get denomination
	#The resulting stack that is retrieved is saved in rawStackFromWithdrawal
	def getReceiptFromCloudBank(self):
		"""<summary>Retrieves CloudCoins from CloudService server that this object holds the keys for.
		The amount withdrawn is the same as the amount last deposited with sendStackToCloudBank.</summary>
		"""
		#var formContent = new FormUrlEncodedContent(new[] { new KeyValuePair<string,string>("rn",receiptNumber),
		# new KeyValuePair<string, string>("pk", keys.privatekey), new KeyValuePair<string, string>("account", keys.account) });
		try:
			result_receipt = self._cli.GetAsync("https://" + self._keys.publickey + "/get_receipt.aspx?rn=" + self._receiptNumber + "&account=" + self._keys.account)
			rawReceipt = result_receipt.Content.ReadAsStringAsync()
			deserialReceipt = JsonConvert.DeserializeObject(self._rawReceipt)
			i = 0
			while i < deserialReceipt.rd.Length:
				if deserialReceipt.rd[i].status == "authentic":
					self._totalCoinsWithdrawn += self.getDenomination(deserialReceipt.rd[i].sn)
				i += 1
		except HttpRequestException, ex:
			Console.Out.WriteLine("Exception: " + ex.Message)
			Console.Out.WriteLine("Check your connection, or your public key")
			return 
		except JsonReaderException, ex:
			Console.Out.WriteLine(ex.Message)
			Console.Out.WriteLine(self._rawReceipt)
			return 
		except JsonSerializationException, ex:
			Console.Out.WriteLine(ex.Message)
			Console.Out.WriteLine(self._rawReceipt)
			return 
		finally:
		try:
			#var formContent2 = new FormUrlEncodedContent(new[] { new KeyValuePair<string,string>("amount",totalCoinsWithdrawn.ToString()),
			#new KeyValuePair<string, string>("pk", keys.privatekey), new KeyValuePair<string, string>("account", keys.account) });
			result_stack = self._cli.GetAsync("https://" + self._keys.publickey + "/withdraw_one_stack.aspx?pk=" + self._keys.privatekey + "&amount=" + self._totalCoinsWithdrawn.ToString() + "&account=" + self._keys.account)
			self._rawStackFromWithdrawal = result_stack.Content.ReadAsStringAsync()
			failResponse = JsonConvert.DeserializeObject(self._rawStackFromWithdrawal)
			Console.Out.WriteLine(failResponse.status)
			Console.Out.WriteLine(failResponse.message)
		except JsonReaderException, ex:
			Console.Out.WriteLine(self._rawStackFromWithdrawal)
		except JsonSerializationException, ex:
			Console.Out.WriteLine(self._rawStackFromWithdrawal)
		except HttpRequestException, ex:
			Console.Out.WriteLine("Exception: " + ex.Message)
			Console.Out.WriteLine("Check your connection, or your public key")
		finally:

	def interpretReceipt(self):
		"""<summary>Parses pertinent information from the receipt last gathered by getReceipt and returns it in the form of an Interpretation object</summary>"""
		inter = Interpretation()
		interpretation = ""
		try:
			#tell the client how many coins were uploaded how many counterfeit, etc.
			deserialReceipt = JsonConvert.DeserializeObject(self._rawReceipt)
			totalNotes = deserialReceipt.total_authentic + deserialReceipt.total_fracked
			totalCoins = 0
			i = 0
			while i < deserialReceipt.rd.Length:
				if deserialReceipt.rd[i].status == "authentic":
					totalCoins += self.getDenomination(deserialReceipt.rd[i].sn)
				i += 1
			interpretation = "receipt number: " + deserialReceipt.receipt_id + " total authentic notes: " + totalNotes + " total authentic coins: " + totalCoins
			inter.interpretation = interpretation
			inter.receipt = deserialReceipt
			inter.totalAuthenticCoins = totalCoins
			inter.totalAuthenticNotes = totalNotes
		except JsonSerializationException, ex:
			Console.Out.WriteLine(ex.Message)
			interpretation = self._rawReceipt
		except JsonReaderException, ex:
			Console.Out.WriteLine(ex.Message)
			interpretation = self._rawReceipt
		finally:
		return inter

	def saveStackToFile(self, path):
		"""<summary>Writes a CloudCoin stack file for the CloudCoin retrieved the last call of either getStackFromCloudBank or getReceiptFromCloudBank</summary>
		<param name="path">The full file path where the new file will be written</param> 
		"""
		File.WriteAllText(path + self.getStackName(), self._rawStackFromWithdrawal)

	#WriteFile(path + stackName, rawStackFromWithdrawal);
	def getStackName(self):
		"""<summary>Generates a filename for the CloudCoin stack file to be written by saveStackToFile</summary>"""
		if self._receiptNumber == None:
			date = DateTime.Now
			tag = "Withdrawal" + date.ToString("MMddyyyyhhmmsff")
			return self._totalCoinsWithdrawn + ".CloudCoin." + tag + ".stack"
		return self._totalCoinsWithdrawn + ".CloudCoin." + self._receiptNumber + ".stack"

	def transferCloudCoins(self, toPublicKey, coinsToSend):
		"""<summary>Calls getStackFromCloudBank and sendStackToCloudBank in order to transfer CloudCoins from one CloudService to another</summary>
		<param name="coinsToSend">The amount of CloudCoins to be transfered</param>
		<param name="toPublicKey"> The public url of the CloudService that is receiving the CloudCoins</param>
		"""
		#Download amount
		self.getStackFromCloudBank(coinsToSend)
		self._rawStackForDeposit = self._rawStackFromWithdrawal #Make it so it will send the stack it recieved
		self.sendStackToCloudBank(toPublicKey)
