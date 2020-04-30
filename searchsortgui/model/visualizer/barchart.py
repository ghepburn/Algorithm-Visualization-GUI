from .canvas.pyqt5_barchart import BarChartCanvas
from .display.display import Display


class BarChart(Display):
	def __init__(self):
		super().__init__()
		self.setCanvas(BarChartCanvas())

