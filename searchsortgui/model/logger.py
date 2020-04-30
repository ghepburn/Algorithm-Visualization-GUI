from .subject.subject import Subject

class Logger(Subject):
	def __init__(self):
		super().__init__()
		self._row = 0

	def getRow(self):
		return self._row

	def setRow(self, number):
		self._row = number

	def incrementRow(self):
		row = self.getRow()
		row += 1
		self.setRow(row)

	def log(self, action, algorithm=None):
		row = self.getRow()	
		self.notifyObservers(log=[row, action, algorithm])

	def clear(self):
		self.notifyObservers(log="clear_log")
