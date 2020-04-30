import matplotlib

# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class PyQt5Canvas(FigureCanvas):
	def __init__(self):
		self.chart_width = 5 
		self.chart_height = 4 
		self.chart_dpi = 100
		self.figure = Figure(figsize=(self.chart_width, self.chart_height), dpi=self.chart_dpi)

	def createDisplay(self, content, colourInput):
		pass

	def generate(self, parent):
		super().__init__(self.figure)
		self.setParent(parent)
		FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		FigureCanvas.updateGeometry(self)