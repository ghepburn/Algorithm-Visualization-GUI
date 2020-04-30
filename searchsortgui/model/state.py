import random
from .subject.subject import Subject
from .visualizer.barchart import BarChart

class State(Subject):
	def __init__(self):
		super().__init__()
		self.Visualizer = BarChart()
		self._quantities = ["10", "20", "50", "100"]
		self._current_quantity = "10"
		self._numbers = None
		self._display = None
		self.randomizeNumbers()

	def getQuantities(self):
		return self._quantities

	def getCurrentQuantity(self):
		return self._current_quantity

	def setCurrentQuantity(self, requested_quantity):
		self._current_quantity = requested_quantity

	def getNumbers(self):
		return self._numbers

	def setNumbers(self, requested_numbers):
		self._numbers = requested_numbers

	def randomizeNumbers(self):
		quantity = self.getCurrentQuantity()
		random_numbers = random.sample(range((int(quantity)*2)), int(quantity))
		self.setNumbers(random_numbers)
		return random_numbers

	def getDisplay(self):
		return self._display

	def setDisplay(self, new_display):
		self._display = new_display
		self.notifyObservers(display=new_display)

	def createDisplay(self, sections=None):
		numbers = self.getNumbers()
		newDisplay = self.Visualizer.create(numbers=numbers, sections=sections)
		self.setDisplay(newDisplay)

	def setupObserver(self, observer):
		quantities = self.getQuantities()
		observer.notify(quantities=quantities)
	




