import datetime as dt


class Timer():
	def __init__(self):
		self._start = None

	def getStart(self):
		return self._start

	def start(self):
		self._start = dt.datetime.now()

	def end(self):
		end = dt.datetime.now()
		start = self.getStart()
		total_time = (end - start).total_seconds()
		return total_time