

class Subject():
	def __init__(self):
		self._observers = []

	def addObserver(self, observer):
		self._observers.append(observer)
		self.setupObserver(observer)

	def removeObserver(self, observer):
		self._observers.remove(observer)

	def getObservers(self):
		return self._observers

	def notifyObservers(self, **kwargs):
		for observer in self._observers:
			observer.notify(**kwargs)

	def setupObserver(self, observer):
		pass
