

class Controller():
	def __init__(self):
		self.stateModel = None
		self.algorithmModel = None
		self.logModel = None
		self.alertModel = None

	def connectToModels(self, **kwargs):
		for kwarg in kwargs:
			if kwarg == "state":
				self.stateModel = kwargs[kwarg]
			elif kwarg == "algorithm":
				self.algorithmModel = kwargs[kwarg]
			elif kwarg == "logger":
				self.logModel = kwargs[kwarg]
			elif kwarg == "alert":
				self.alertModel = kwargs[kwarg]

	def toggleActionType(self):
		self.algorithmModel.changeCurrentAlgorithmType()

	def changeAlgorithm(self, requested_algorithm, search_target=None):
		if len(requested_algorithm) > 1:
			numbers = self.stateModel.getNumbers()
			self.algorithmModel.setCurrentState(number_list=numbers, requested_algorithm=requested_algorithm, search_target=search_target)
			self.logModel.log(action="Changed Algorithm", algorithm=requested_algorithm)
			self.alertModel.scan(requested_algorithm)

	def changeQuantity(self, requested_quantity):
		if requested_quantity != None:
			self.stateModel.setCurrentQuantity(requested_quantity)
		self.logModel.log(action=f"Changed Quantity To {requested_quantity}")

	def initializeDisplay(self):
		numbers = self.stateModel.randomizeNumbers()
		self.algorithmModel.setCurrentState(numbers)
		self.stateModel.createDisplay()
		self.logModel.clear()

	def advanceDisplay(self):
		try:
			processed_numbers, index_sections, action = self.algorithmModel.executeAlgorithm()
			self.stateModel.setNumbers(processed_numbers)
			self.stateModel.createDisplay(index_sections)

			current_algorithm = self.algorithmModel.getCurrentAlgorithm().getName()
			self.logModel.log(action=action, algorithm=current_algorithm)
		except:
			pass

	def finishDisplay(self):
		try:
			finished_numbers, index_sections, action = self.algorithmModel.finishAlgorithm()
			self.stateModel.setNumbers(finished_numbers)
			self.stateModel.createDisplay(index_sections)
			
			current_algorithm = self.algorithmModel.getCurrentAlgorithm().getName()
			self.logModel.log(action=action, algorithm=current_algorithm)
		except:
			pass

	def changedSearchInput(self, search_target):
		current_algorithm_name = self.algorithmModel.getCurrentAlgorithm().getName()
		self.changeAlgorithm(requested_algorithm=current_algorithm_name, search_target=search_target)
