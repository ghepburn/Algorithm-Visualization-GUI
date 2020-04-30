from .subject.subject import Subject

class Alert(Subject):
	def __init__(self):
		super().__init__()
		self._colour = "Red"
		self._alerts = {"Binary_Search": "Numbers Must Be Sorted!"}

	def addAlert(self, name, message):
		self._alerts[object] = message

	def getAlert(self, name):
		return self._alerts[name]

	def isAlert(self, name):
		return name in self._alerts

	def scan(self, *args):
		for arg in args:
			if self.isAlert(arg):
				alert = self.getAlert(arg)
				self.notifyObservers(alert=alert)
			else:
				self.notifyObservers(alert=None)