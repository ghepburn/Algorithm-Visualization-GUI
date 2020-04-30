from PyQt5 import QtCore, QtGui, QtWidgets

from .observer.observer import Observer
from .ui.pyqt5ui import UserInterface


class View(UserInterface, Observer):
	def __init__(self, MainWindow):
		super().__init__(MainWindow)

	def subscribeToModels(self, *args):
		for model in args:
			model.addObserver(self)

	def connectToController(self, controller):
		self.initButton.clicked.connect(controller.initializeDisplay)
		self.stepButton.clicked.connect(controller.advanceDisplay)
		self.finishButton.clicked.connect(controller.finishDisplay)
		self.actionToggleButton.clicked.connect(controller.toggleActionType)
		self.numQtyComboBox.currentIndexChanged.connect(lambda: controller.changeQuantity(self.numQtyComboBox.currentText()))
		self.algoComboBox.currentIndexChanged.connect(lambda: controller.changeAlgorithm(self.algoComboBox.currentText()))
		self.searchInput.textChanged.connect(lambda: controller.changedSearchInput(self.searchInput.text()))

	def setActionTypeLabel(self, requested_label):
		self.actionTypeLabel.setText(requested_label)

	def setAlgorithmList(self, requested_algorithm_list):
		self.algoComboBox.clear()
		for algorithm in requested_algorithm_list:
			self.algoComboBox.addItem(algorithm)

	def setQuantityList(self, requested_quantity_list):
		self.numQtyComboBox.clear()
		for quantity in requested_quantity_list:
			self.numQtyComboBox.addItem(quantity)

	def setDisplay(self, requested_display):
		parent = self.verticalLayoutWidget_9
		requested_display.generate(parent)
		while self.displayLayout.count() > 0:
			self.displayLayout.takeAt(0)
		self.displayLayout.addWidget(requested_display)

	def notifyUser(self, message):
		messageContainer = QtWidgets.QMessageBox()
		messageContainer.setWindowTitle("User Notification")
		messageContainer.setText(message)
		messageContainer.exec_()

	def setRuntime(self, runtime):
		self.runtimeNumber.display(runtime)

	def enterLog(self, row, action, algorithm=None):
		self.displayTable.insertRow(row)
		if algorithm:
			cell1 = QtWidgets.QTableWidgetItem(algorithm)
			cell1.setTextAlignment(QtCore.Qt.AlignCenter)
			self.displayTable.setItem(row, 0, cell1)
		cell2 = QtWidgets.QTableWidgetItem(action)
		cell2.setTextAlignment(QtCore.Qt.AlignCenter)
		self.displayTable.setItem(row, 1, cell2)

	def clearLog(self):
		self.displayTable.clear()
		self.displayTable.setRowCount(0)

	def setAlert(self, message):
		if message != None:
			self.alertMessage.setText(message)	
			self.alertMessage.setStyleSheet("QLabel#alertMessage {color: red}")
			self.alertLabel.setText("Notice:")	
			self.alertLabel.setStyleSheet("QLabel#alertLabel {color: red}")	
		else:
			self.alertMessage.setText("")	
			self.alertLabel.setText("")		

	def notify(self, **kwargs):
		for kwarg in kwargs:
			if kwarg == "algorithm_type":
				self.setActionTypeLabel(kwargs[kwarg])
			elif kwarg == "algorithm_list":
				self.setAlgorithmList(kwargs[kwarg])
			elif kwarg == "quantities":
				self.setQuantityList(kwargs[kwarg])
			elif kwarg == "display":
				self.setDisplay(kwargs[kwarg])
			elif kwarg == "message":
				self.notifyUser(kwargs[kwarg])
			elif kwarg == "runtime":
				self.setRuntime(kwargs[kwarg])
			elif kwarg == "log":
				log = kwargs[kwarg]
				if log == "clear_log":
					self.clearLog()
				else:
					self.enterLog(log[0], log[1], log[2])
			elif kwarg == "alert":
				self.setAlert(kwargs[kwarg])
