from .algorithm import Algorithm
from .DataStructures.HashTable import HashTable
from .DataStructures.Tree import BinaryTree, AVLSearchTree

class SearchAlgorithm(Algorithm):
	def __init__(self):
		super().__init__()
		self._target = None
		self.setType("search")

	def getTarget(self):
		return self._target

	def setTarget(self, number):
		self._target=number
		

class SequentialSearchAlgorithm(SearchAlgorithm):
	def __init__(self):
		super().__init__()
		self.setName("Sequential_Search")

	def execute(self, numberList):
		target = self.getTarget()
		position = 0
		found = False
		while not found and position <= len(numberList)-1:
			if numberList[position] == target:
				found = True
				yield numberList, [[position], [position], [position]], f"Located {target}"
			else:
				yield numberList, [[position]], "Searching"
				position += 1


class BinarySearchAlgorithm(SearchAlgorithm):
	def __init__(self):
		super().__init__()
		self.setName("Binary_Search")

	def execute(self, numberList):
		target = self.getTarget()
		first = 0
		last = len(numberList)-1
		found = False
		index = False

		while first <= last and not found:

			midpoint = (first+last)//2

			yield numberList, [[midpoint], [midpoint]], "Divide Numbers"

			if numberList[midpoint] == target:
				found = True
				index = midpoint
				yield numberList, [[index], [index], [index]], f"Located {target}"
			else:
				if target < numberList[midpoint]:
					last = midpoint - 1
				else:
					first = midpoint + 1

				yield numberList, [[x for x in range(first, last+1)]], "Higher or Lower"

class HashTableSearchAlgorithm(HashTable, SearchAlgorithm):
	def __init__(self):
		super().__init__()
		SearchAlgorithm.__init__(self)
		self.setName("HashTable_Search")
		self.numberList = None

	def execute(self, numberList):
		print("execute")
		target = self.getTarget()
		self.numberList = numberList
		self.inputList(numberList)
		yield from self.get(target)
		
	def get(self, key):
		found = False
		stop = False
		data = False
		hashed_value = self.hash(key)
		position = hashed_value
		while not found and not stop and self.slots[position] != None:
			yield self.numberList, [[self.data[position]]], "Searching"
			if self.slots[position] == key:
				found = True
				data = self.data[position]
				yield self.numberList, [[data], [data], [data]], f"Located {target}"
			else:
				position = self.rehash(position)
				if position == hashed_value:
					stop = True
					yield self.numberList, [[self.data[position]], [self.data[position]], [self.data[position]]], f"located {target}"


class BinaryTreeSearchAlgorithm(SearchAlgorithm, BinaryTree):
	def __init__(self):
		super().__init__()
		BinaryTree.__init__(self)
		self.name = self.setName("BinaryTree_Search")
		self.numberList = None

	def execute(self, numberList):
		target = self.getTarget()
		self.numberList = numberList
		self.generateTree(numberList)
		yield from self.get(target)

	def get(self, target):
		key = target
		if self.root:
			yield from self._get(key, self.root)
		else:
			yield self.numberList, [[key], [key], [key]], f"Located {target}"

	def _get(self, key, currentNode):

		yield self.numberList, [[currentNode.payload]], "Searching"

		if currentNode.key == key:
			yield self.numberList, [[currentNode.payload], [currentNode.payload], [currentNode.payload]], f"Located {target}"

		elif key < currentNode.key:
			yield from self._get(key, currentNode.getLeftChild())
		
		else:
			yield from self._get(key, currentNode.getRightChild())



class AVLTreeSearchAlgorithm(SearchAlgorithm, AVLSearchTree):
	def __init__(self):
		super().__init__()
		AVLSearchTree.__init__(self)
		self.setName("AVLTree_Search")
		self.numberList = None

	def execute(self, numberList):
		target = self.getTarget()
		self.numberList = numberList
		self.generateTree(numberList)
		yield from self.get(target)

	def get(self, target):
		key = target
		if self.root:
			yield from self._get(key, self.root)
		else:
			yield self.numberList, [[key],[key], [key]], f"Located {target}"

	def _get(self, key, currentNode):

		yield self.numberList, [[currentNode.payload]], "Searching"

		if currentNode.key == key:
			yield self.numberList, [[currentNode.payload], [currentNode.payload], [currentNode.payload]], f"Located {target}"

		elif key < currentNode.key:
			yield from self._get(key, currentNode.getLeftChild())
		
		else:
			yield from self._get(key, currentNode.getRightChild())
