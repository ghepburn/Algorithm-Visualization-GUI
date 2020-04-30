class Algorithm():
	def __init__(self):
		self._name = None
		self._type = None

	def getName(self):
		return self._name

	def setName(self, requested_name):
		self._name = requested_name

	def getType(self):
		return self._type

	def setType(self, requested_type):
		self._type = requested_type

	def execute(self, numberList):
		pass