from System import *
from banktesterforms import *
from System.Threading.Tasks import *
from System.Net.Http import *
from System.IO import *

class Program(object):
	def __init__(self):
		# INSTANCE VARIABLES
		self._reader = KeyboardReader()
		#  public static String rootFolder = System.getProperty("user.dir") + File.separator +"bank" + File.separator ;
		self._rootFolder = AppDomain.CurrentDomain.BaseDirectory
		self._prompt = "Start Mode> "
		self._commandsAvailable = Array[String](("Load Bank Keys", "Show Coins", "Deposite Coin", "Withdraw Coins", "Look at Receipt", "Write Check", "Get Check", "Connect To Trusted Trade", "Send Coins Over Trusted Trade", "quit"))
		#public static int timeout = 10000; // Milliseconds to wait until the request is ended. 
		# public static FileUtils fileUtils = new FileUtils(rootFolder, bank);
		self._myRandom = Random()
		self._publicKey = ""
		self._privateKey = ""
		self._email = ""
		self._sign = "Preston Linderman"
		self._cli = HttpClient()
		self._tts = TrustedTradeSocket("wss://escrow.cloudcoin.digital/ws/", 10, OnWord, OnStatusChange, OnReceive, OnProgress)

	# MAIN METHOD
	def Main(args):
		Program.printWelcome()
		Program.run().Wait() # Makes all commands available and loops
		Console.Out.WriteLine("Thank you for using CloudBank Tester. Goodbye.")

	Main = staticmethod(Main)
 # End main
	# STATIC METHODS
	def run():
		restart = False
		while not restart:
			Console.ForegroundColor = ConsoleColor.Green
			Console.Out.WriteLine("")
			#  Console.Out.WriteLine("========================================");
			Console.Out.WriteLine("")
			Console.Out.WriteLine("Commands Available:")
			Console.ForegroundColor = ConsoleColor.White
			commandCounter = 1
			enumerator = commandsAvailable.GetEnumerator()
			while enumerator.MoveNext():
				command = enumerator.Current
				Console.Out.WriteLine(commandCounter + (". " + command))
				commandCounter += 1
			Console.ForegroundColor = ConsoleColor.Green
			Console.Out.Write(self._prompt)
			Console.ForegroundColor = ConsoleColor.White
			commandRecieved = self._reader.readInt(1, 10)
			if commandRecieved == 1:
				Program.loadKeys()
			elif commandRecieved == 2:
				Program.showCoins()
			elif commandRecieved == 3:
				self._receiptHolder = Program.depositAsync()
			elif commandRecieved == 4:
				Program.withdraw()
			elif commandRecieved == 5:
				Program.receipt2()
			elif commandRecieved == 6:
				Program.writeCheck()
			elif commandRecieved == 7:
				Program.GetCheck()
			elif commandRecieved == 8:
				self._tts.Connect()
			elif commandRecieved == 9:
				Program.SendCoinsTT()
			elif commandRecieved == 10:
				Console.Out.WriteLine("Goodbye!")
				Environment.Exit(0)
			else:
				Console.Out.WriteLine("Command failed. Try again.")

	run = staticmethod(run)
 # end switch # end while # end run method
	def printWelcome():
		Console.ForegroundColor = ConsoleColor.Green
		Console.Out.WriteLine("╔══════════════════════════════════════════════════════════════════╗")
		Console.Out.WriteLine("║                   CloudBank Tester v.11.19.17                    ║")
		Console.Out.WriteLine("║          Used to Authenticate Test CloudBank                     ║")
		Console.Out.WriteLine("║      This Software is provided as is with all faults, defects    ║")
		Console.Out.WriteLine("║          and errors, and without warranty of any kind.           ║")
		Console.Out.WriteLine("║                Free from the CloudCoin Consortium.               ║")
		Console.Out.WriteLine("╚══════════════════════════════════════════════════════════════════╝")
		Console.ForegroundColor = ConsoleColor.White

	printWelcome = staticmethod(printWelcome)
 # End print welcome
	def loadKeys():
		self._publicKey = "bank.CloudCoin.global"
		self._privateKey = "0DECE3AF-43EC-435B-8C39-E2A5D0EA8676"
		self._email = "Preston@ChicoHolo.com"
		Console.Out.WriteLine("Public key is " + self._publicKey)
		Console.Out.WriteLine("Private key is " + self._privateKey)
		Console.Out.WriteLine("Email is " + self._email)
		self._myKeys = BankKeys(self._publicKey, self._privateKey, self._email)

	loadKeys = staticmethod(loadKeys)

	# Show coins will populate the CloudBankUtils with the totals of each denominations
	# These totals are public properties that can be accessed
	def showCoins():
		cbu = CloudBankUtils(self._myKeys)
		cbu.showCoins()
		Console.Out.WriteLine("Ones in our bank:" + cbu.onesInBank)
		Console.Out.WriteLine("Five in our bank:" + cbu.fivesInBank)
		Console.Out.WriteLine("Twenty Fives in our bank:" + cbu.twentyFivesInBank)
		Console.Out.WriteLine("Hundreds in our bank:" + cbu.hundresInBank)
		Console.Out.WriteLine("Two Hundred Fifties in our bank:" + cbu.twohundredfiftiesInBank)

	showCoins = staticmethod(showCoins)
 #end show coins
	# Deposit allow you to send a stack file to the CloudBank
	def depositAsync():
		sender = CloudBankUtils(self._myKeys)
		Console.Out.WriteLine("What is the path to your stack file?")
		#string path = reader.readString();
		path = AppDomain.CurrentDomain.BaseDirectory
		path += self._reader.readString()
		Console.Out.WriteLine("Loading " + path)
		sender.loadStackFromFile(path)
		sender.sendStackToCloudBank(self._publicKey)
		sender.getReceipt(self._publicKey)
		return sender

	depositAsync = staticmethod(depositAsync)
 #end deposit
	def withdraw():
		if self._receiptHolder == None:
			receiver = CloudBankUtils(self._myKeys)
		else:
			receiver = self._receiptHolder
		Console.Out.WriteLine("How many CloudCoins are you withdrawing?")
		amount = self._reader.readInt()
		receiver.getStackFromCloudBank(amount)
		receiver.saveStackToFile(AppDomain.CurrentDomain.BaseDirectory)

	withdraw = staticmethod(withdraw)
 #end deposit
	def receipt():
		if self._receiptHolder == None:
			Console.Out.WriteLine("There has not been a recent deposit. So no receipt can be shown.")
		else:
			Console.Out.WriteLine(self._receiptHolder.interpretReceipt())

	receipt = staticmethod(receipt)
 #end deposit
	def receipt2():
		x = CloudBankUtils(self._myKeys)
		x.getReceipt(self._myKeys.publickey)

	receipt2 = staticmethod(receipt2)

	def writeCheck():
		Console.Out.WriteLine("How many CloudCoins are you withdrawing?")
		amount = self._reader.readInt()
		Console.Out.WriteLine("Who are you Paying?")
		payto = self._reader.readString()
		Console.Out.WriteLine("Who is being Emailed?")
		emailto = self._reader.readString()
		request = self._cli.GetAsync("https://" + self._publicKey + "/write_check.aspx?pk=" + self._privateKey + "&action=email&amount=" + amount + "&emailto=" + emailto + "&payto=" + payto + "&from=" + self._email + "&signby=" + self._sign)
		response = request.Content.ReadAsStringAsync()
		Console.Out.WriteLine(response)

	writeCheck = staticmethod(writeCheck)

	def GetCheck():
		Console.Out.WriteLine("What is the Check's Id?")
		id = self._reader.readString()
		request = self._cli.GetAsync("https://" + self._publicKey + "/checks.aspx?id=" + id + "&receive=json")
		response = request.Content.ReadAsStringAsync()
		Console.Out.WriteLine(response)

	GetCheck = staticmethod(GetCheck)

	def SendCoinsTT():
		Console.Out.WriteLine("What is the recipients secred word?")
		word = self._reader.readString()
		Console.Out.WriteLine("What is the path to your stack file?")
		#string path = reader.readString();
		path = AppDomain.CurrentDomain.BaseDirectory
		path += self._reader.readString()
		Console.Out.WriteLine("Loading " + path)
		stack = File.ReadAllText(path)
		self._tts.SendCoins(word, stack)

	SendCoinsTT = staticmethod(SendCoinsTT)

	def OnProgress(i):
		Console.WriteLine("Progress" + i + "%")
		return True

	OnProgress = staticmethod(OnProgress)

	def OnWord(word):
		self._tts.secretWord = word
		Console.WriteLine("word: " + word)
		return True

	OnWord = staticmethod(OnWord)

	def OnReceive(hash):
		Console.WriteLine("https://escrow.cloudcoin.digital/cc.php?h=" + hash)
		return True

	OnReceive = staticmethod(OnReceive)

	def OnStatusChange():
		Console.WriteLine("Status Changed")
		return True

	OnStatusChange = staticmethod(OnStatusChange)
