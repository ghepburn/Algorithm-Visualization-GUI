from .algorithms.SearchAlgorithm import SequentialSearchAlgorithm, BinarySearchAlgorithm, HashTableSearchAlgorithm, BinaryTreeSearchAlgorithm, AVLTreeSearchAlgorithm
from .algorithms.SortAlgorithm import BubbleSortAlgorithm, InsertSortAlgorithm, SelectionSortAlgorithm, MergeSortAlgorithm, ShellSortAlgorithm, QuickSortAlgorithm
		
import copy

class SearchSortAlgorithmFactory():
	def __init__(self):
		self._algorithms = [BubbleSortAlgorithm(), InsertSortAlgorithm(), SelectionSortAlgorithm(), MergeSortAlgorithm(), ShellSortAlgorithm(), QuickSortAlgorithm(), SequentialSearchAlgorithm(), BinarySearchAlgorithm(), HashTableSearchAlgorithm(), BinaryTreeSearchAlgorithm(), AVLTreeSearchAlgorithm()]
		self._algorithm_types = ["sort", "search"]

	def getAlgorithm(self, algorithm_name):
		for algorithm in self._algorithms:
			if algorithm.getName() == algorithm_name:
				identified_algorithm = copy.deepcopy(algorithm)
				return identified_algorithm
		return print(f"No Algorithm With The Name {algorithm_name} --AlgoFactory")

	def getAlgorithmTypes(self):
		return self._algorithm_types

	def getAllAlgorithms(self):
		return self._algorithms

	def getAlgorithmList(self, **kwargs):
		results = []
		algorithms = self.getAllAlgorithms()
		for kwarg in kwargs:
			if kwarg == "type":
				for algo_type in self.getAlgorithmTypes():
					if kwargs[kwarg] == algo_type:
						for algorithm in algorithms:
							if algorithm.getType() == algo_type:
								results.append(algorithm.getName())
		return results

	def setTarget(self, number):
		for algorithm in self._algorithms:
			if algorithm.getType() == "search":
				algorithm.setTarget(int(number))