from System import *
from System.Text import *
from System.Linq import *

class KeyboardReader(object):
	def __init__(self):
		self._INT_MESSAGE = 0
		self._DOUBLE_MESSAGE = 1
		self._CHAR_MESSAGE = 2
		self._STRING_MESSAGE = 3
		self._BOOLEAN_MESSAGE = 4
		self._LONG_MESSAGE = 5
		self._NUM_ERROR_MESSAGES = 6
		self._prompt = "> "
		self._prompt = "> "

	def setPrompt(self, newPrompt):
		self._prompt = newPrompt

	def readString(self):
		theChar = 'x'
		result = ""
		done = False
		while not done:
			theChar = self.nextChar()
			if (theChar == '\n'):
				done = True
			elif (theChar == '\r'):
			else:
				result = (result + theChar)
		return result

	def readString(self, args):
		result = self.readString()
		result = result.ToLower()
		while not args.Any(result.Contains):
			Console.Out.WriteLine("  Please enter one of the following: " + self.ConvertStringArrayToString(args)) # "Please enter one of the following: " );
			Console.Out.Write(self._prompt)
			result = self.readString(args)
		return result

	def readInt(self):
		inputString = ""
		number = 0
		done = False
		while not done:
			try:
				inputString = self.readString()
				inputString = inputString.Trim()
				number = Convert.ToInt32(inputString)
				done = True
			except FormatException, e:
				Console.Out.WriteLine("  Input is not an integer. " + self._errorMessages[self._INT_MESSAGE]) # "Input is not an integer. ";
				#CoreLogger.Log("  Input is not an integer. " + this.errorMessages[INT_MESSAGE]);
				# CoreLogger.Log(e.ToString());
				Console.Out.Write(self._prompt)
			finally:
		return number

	def readInt(self, min, max):
		inputString = ""
		number = 0
		done = False
		while not done:
			try:
				inputString = self.readString()
				inputString = inputString.Trim()
				number = Convert.ToInt32(inputString)
				if ((number < min) or (number > max)):
					Console.Out.WriteLine("  Please enter an integer between " + min + " & " + max)
				else: #"Please enter an integer between " 
					done = True
			except FormatException, e:
				Console.Out.WriteLine("  Input is not an integer. Please enter an integer between " + min + " & " + max) #"Input is not an integer. Please enter an integer between " 
				# CoreLogger.Log("  Input is not an integer. Please enter an integer between " + min + " & " + max);
				# CoreLogger.Log(e.ToString());
				Console.Out.Write(self._prompt)
			finally:
		return number

	def readInt(self, args):
		result = self.readInt()
		while not self.checkInArray(result, args):
			Console.Out.WriteLine("  Please enter one of the following: " + str.Join(",", args)) # "Please enter one of the following: "
			Console.Out.Write(self._prompt)
			result = self.readInt(args)
		return result

	def checkInArray(self, currentState, myArray):
		found = False
		i = 0
		while (not found and (i < myArray.Length)):
			found = (myArray[i] == currentState)
			i += 1
		return found

	def ConvertStringArrayToString(array):
		#
		# Concatenate all the elements into a StringBuilder.
		#
		builder = StringBuilder()
		enumerator = array.GetEnumerator()
		while enumerator.MoveNext():
			value = enumerator.Current
			builder.Append(value)
			builder.Append(' ')
		return builder.ToString()

	ConvertStringArrayToString = staticmethod(ConvertStringArrayToString)
 #End convert string array to string
	# *
	# * Use System.in.read to read the next character from the
	# * STDIN stream.
	# 
	def nextChar(self):
		charAsInt = -1
		try:
			charAsInt = Console.Read()
		except InvalidOperationException, e:
			Console.WriteLine(e)
			#  CoreLogger.Log(e.ToString());
			Console.WriteLine("  Fatal error. Exiting program.") # "Fatal error. Exiting program.");
			return charAsInt
		finally:
		return charAsInt
