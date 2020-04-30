from PyQt5 import QtWidgets
import sys

from view.view import View
from controller.controller import Controller
from model.algorithm import Algorithm
from model.state import State
from model.logger import Logger
from model.alert import Alert

if __name__ == "__main__":
    
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()

	algorithm = Algorithm()
	state = State()
	logger = Logger()
	alert = Alert()

	controller = Controller() 
	controller.connectToModels(algorithm=algorithm, state=state, logger=logger, alert=alert)

	ui = View(MainWindow)
	ui.connectToController(controller)
	ui.subscribeToModels(algorithm, state, logger, alert)

	# controller = SearchSortUIController(ui)

	MainWindow.show()
	sys.exit(app.exec_())