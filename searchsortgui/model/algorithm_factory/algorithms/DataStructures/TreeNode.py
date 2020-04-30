class TreeNode():
	def __init__(self, key, val, left=None, right=None, parent=None):
		self.key = key
		self.payload = val
		self.leftChild = left
		self.rightChild = right
		self.parent = parent
		self.balanceFactor = 0

	def hasLeftChild(self):
		return self.leftChild != None

	def hasRightChild(self):
		return self.rightChild != None

	def getLeftChild(self):
		return self.leftChild

	def getRightChild(self):
		return self.rightChild

	def isLeftChild(self):
		return self.parent != None and self.parent.leftChild == self

	def isRightChild(self):
		return self.parent != None and self.parent.rightChild == self

	def isRoot(self):
		return self.parent == None

	def isLeaf(self):
		return (self.rightChild and self.leftChild) == None

	def hasAnyChildren(self):
		return (self.rightChild or self.leftChild) != None

	def hasBothChildren(self):
		return (self.rightChild and self.leftChild) != None

	def replaceNodeData(self, key, value, lc, rc):
		self.key = key
		self.value = value
		self.leftChild = lc
		self.rightChild = rc
		if self.hasLeftChild():
			self.leftChild.parent = self
		if self.hasRightChild():
			self.rightChild.parent = self

	def findSuccesor(self):
		succ = None
		if self.hasRightChild():
			succ = self.rightChild.findMin()
		else:
			if self.parent:
				if self.isLeftChild():
					succ = self.parent
				else:
					self.parent.rightChild = None
					succ = self.parent.findSuccesor()
					self.parent.rightChild = self
		return succ

	def findMin(self):
		current = self
		while current.hasLeftChild():
			current = current.leftChild
		return current

	def spliceOut(self):
		if self.isLeaf():
			if self.isLeftChild():
				self.parent.leftChild = None
			else:
				self.parent.rightChild = None
		elif self.hasAnyChildren():
			if self.hasLeftChild():
				self.leftChild.parent = self.parent
				if self.isLeftChild():
					self.parent.leftChild = self.leftChild
				else:
					self.parent.rightChild = self.leftChild
			else:
				self.rightChild.parent = self.parent
				if self.isLeftChild():
					self.parent.leftChild = self.rightChild
				else:
					self.parent.rightChild = self.rightChild
	
	def __iter__(self):
		if self:
			if self.hasLeftChild():
				for i in self.leftChild:
					yield i
			yield self.key
			if self.hasRightChild():
				for i in self.rightChild:
					yield i