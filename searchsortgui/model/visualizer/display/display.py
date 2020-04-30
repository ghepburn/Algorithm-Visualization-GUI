

class Display():
	def __init__(self):
		self._canvas = None
		self._numbers = []
		self._colours = ["Blue", "Yellow", "Red", "Green", "Purple"]
		self._colour_input_list = []

	def getCanvas(self):
		return self._canvas

	def setCanvas(self, requested_canvas):
		self._canvas = requested_canvas

	def getNumbers(self):
		return self._numbers

	def setNumbers(self, requested_numbers):
		self._numbers = requested_numbers
		main_colour = self.getColours()[0]
		quantity = len(requested_numbers)
		self.setColourInputList(main_colour, quantity)

	def getColours(self):
		return self._colours

	def getColourInputList(self):
		return self._colour_input_list

	def setColourInputList(self, colour, quantity):
		self._colour_input_list = [colour] * quantity

	def editColourInputList(self, sections_list):
		colour_input_list = self.getColourInputList()
		if len(colour_input_list) > 0:
			colours = self.getColours()
			for count, section in enumerate(sections_list):
				for index in section:
					colour_input_list[index] = colours[count+1]
			self._colour_input_list = colour_input_list

	def create(self, **kwargs):
		for kwarg in kwargs:
			if kwarg == "numbers":
				self.setNumbers(kwargs[kwarg])
			elif kwarg == "sections" and kwargs[kwarg] != None:
				self.editColourInputList(kwargs[kwarg])

		numbers = self.getNumbers()
		colour_input_list = self.getColourInputList()
		canvas = self.getCanvas()
		canvas.createDisplay(numbers, colour_input_list)
		return canvas	