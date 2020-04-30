from .pyqt5.pyqt5canvas import PyQt5Canvas

class BarChartCanvas(PyQt5Canvas):
	def createDisplay(self, content, colourInput):
		self.__init__()
		xValues = [str(number) for number in content] 
		yValues = content
		self.axes = self.figure.add_subplot(111).bar(xValues, yValues, color=colourInput)
