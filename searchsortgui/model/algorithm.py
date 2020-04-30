from .algorithm_factory.search_sort_factory import SearchSortAlgorithmFactory
from .subject.subject import Subject
from .timer import Timer


class Algorithm(Subject):
	def __init__(self):
		super().__init__()
		self.__AlgorithmFactory = SearchSortAlgorithmFactory()
		self.__currentAlgorithm = None
		self.__current_state = None
		self.timer = Timer()

	def getCurrentAlgorithm(self):
		return self.__currentAlgorithm

	def setCurrentAlgorithm(self, requested_algorithm):
		self.__currentAlgorithm = self.__AlgorithmFactory.getAlgorithm(requested_algorithm)
		

	def getCurrentState(self):
		return self.__current_state

	def setCurrentState(self, number_list=None, requested_algorithm=None, search_target=None):
		if search_target:
			self.setNumberTarget(search_target)
		if requested_algorithm:
			self.setCurrentAlgorithm(requested_algorithm)
		if number_list:
			current_algorithm = self.getCurrentAlgorithm()
			self.__current_state = current_algorithm.execute(number_list)

	def setNumberTarget(self, target):
		self.__AlgorithmFactory.setTarget(target)

	def getCurrentAlgorithmType(self):
		return self.__currentAlgorithm.getType()

	def getAlgorithmTypes(self):
		return self.__AlgorithmFactory.getAlgorithmTypes()

	def getAlgorithmList(self, **kwargs):
		return self.__AlgorithmFactory.getAlgorithmList(**kwargs)

	def changeCurrentAlgorithmType(self):
		current_type = self.getCurrentAlgorithmType()
		all_types = self.getAlgorithmTypes()
		for algo_type in all_types:
			if current_type != algo_type:
				new_type_algorithm_list = self.getAlgorithmList(type=algo_type)
				self.notifyObservers(algorithm_type=algo_type, algorithm_list=new_type_algorithm_list)

	def executeAlgorithm(self):
		current_state = self.getCurrentState()
		try:
			return next(current_state)
		except:
			self.algorithmComplete()

	def finishAlgorithm(self):
		done = False
		current_state = self.getCurrentState()
		self.timer.start()
		while not done:
			try:
				processed_state, sections, message = next(current_state)
			except:
				total_runtime = self.timer.end()
				self.notifyObservers(runtime=total_runtime)
				done = True
		try:
			return processed_state, sections, message
		except:
			self.algorithmComplete()

	def algorithmComplete(self):
		current_algorithm = self.getCurrentAlgorithm().getName()
		self.notifyObservers(message=f"{current_algorithm} Algorithm Is Complete")

	def setupObserver(self, observer):
		starting_algorithm_type  = self.getAlgorithmTypes()[0]
		algorithm_list = self.getAlgorithmList(type=starting_algorithm_type)
		observer.notify(algorithm_type=starting_algorithm_type, algorithm_list=algorithm_list)
