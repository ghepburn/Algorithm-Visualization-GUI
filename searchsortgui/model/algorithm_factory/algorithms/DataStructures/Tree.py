from .TreeNode import TreeNode


class BinaryTree():
	def __init__(self):
		super().__init__()
		self.root = None
		self.size = 0


	def generateTree(self, alist):
		for index, num in enumerate(alist):
			self.put(num, index)

	def length(self):
		return self.size

	def __len__(self):
		return self.size

	def __iter__(self):
		return self.root.__iter__()

	def put(self, key, value):
		if self.root:
			self._put(key, value, self.root)
		else:
			self.root = TreeNode(key, value)
		self.size += 1

	def _put(self, key, value, currentNode):
		if key < currentNode.key:
			if currentNode.hasLeftChild():
				self._put(key, value, currentNode.getLeftChild())
			else:
				currentNode.leftChild = TreeNode(key, value, parent=currentNode)
		else:
			if currentNode.hasRightChild():
				self._put(key, value, currentNode.getRightChild())
			else:
				currentNode.rightChild = TreeNode(key, value, parent=currentNode)

	def __setitem__(self, key, value):
		return self.put(key, value)

	def run(self):
		key = self.number
		if self.root:
			yield from self._get(key, self.root)
		else:
			yield [self.signal[3], [False, []]]

	def _get(self, key, currentNode):

		yield [self.signal[0], [False, [currentNode.payload]]]

		if currentNode.key == key:
			yield [self.signal[1], [True, [currentNode.payload]]]

		if key < currentNode.key:
			yield from self._get(key, currentNode.getLeftChild())
		
		else:
			yield from self._get(key, currentNode.getRightChild())

	def __getitem__(self, key):
		return self.get(key)

	def __contains__(self, key):
		return key == self.get(key)

	def delete(self, key):
		if self.size > 1:
			nodeToRemove = self._get(key, self.root)
			if nodeToRemove:
				self.remove(nodeToRemove)
				self.size -= 1
			else:
				raise KeyError("Error, key not in tree you dummy")	
		elif self.size == 1 and self.root.key == key:
			self.root = None
			self.size =- 1
		else:
			raise KeyError("Error, key not in tree you dummy")

	def remove(self, node):
		#Node has no children
		if node.isLeaf():
			if node.isLeftChild():
				node.parent.leftChild = None
			else:
				node.parent.rightChild = None


		#node has two children...yikes
		elif node.hasBothChildren():
			#1. find successor
			#2. remove successor
			#3. replace node with successor
			succ = node.findSuccessor()
			succ.spliceOut()
			node.key = succ.key
			node.payload = succ.payload


		#node has one child

		#1. identify child
		#2. identify parent
		#3. replce parent as nodes parent
		#4. replace child as nodes child

		else:
			#If nodes child is left
			if node.hasLeftChild():
				#if node is a left child of parent
				if node.isLeftChild():
					node.leftChild.parent = node.parent
					node.parent.leftChild = node.leftChild
				#if node is a right child of parent
				elif node.isRightChild():
					node.leftChild.parent = node.parent
					node.parent.rightChild = node.leftChild
				#if node has no parent
				else:
					node.replaceNodeData(node.leftChild.key, 
										node.leftChild.payload, 
										node.leftChild.leftChild, 
										node.leftChild.rightChild)

			#if nodes child is right
			else:
				#if node is a right child of parent
				if node.isLeftChild():
					node.rightChild.parent = node.parent
					node.parent.leftChild = node.rightChild
				#if node is a right child of parent
				elif node.isRightChild():
					node.rightChild.parent = node.parent
					node.parent.rightChild = node.rightChild
				#if node has no parent
				else:
					node.replaceNodeData(node.rightChild.key, 
										node.rightChild.payload, 
										node.rightChild.leftChild, 
										node.rightChild.rightChild)


	def __delitem__(self, key):
		return self.delete(key)


class AVLSearchTree(BinaryTree):
	def __init__(self):
		super().__init__()
		self.name = "AVLSearchTree"

	def _put(self, key, value, currentNode):
		if key < currentNode.key:
			if currentNode.hasLeftChild():
				self._put(key, value, currentNode.getLeftChild())
			else:
				currentNode.leftChild = TreeNode(key, value, parent=currentNode)
				self.updateBalance(currentNode.leftChild)
		else:
			if currentNode.hasRightChild():
				self._put(key, value, currentNode.getRightChild())
			else:
				currentNode.rightChild = TreeNode(key, value, parent=currentNode)
				self.updateBalance(currentNode.rightChild)

	def updateBalance(self, node):

		if node.balanceFactor > 1 or node.balanceFactor < -1:
			self.rebalance(node)
			return
		if node.parent != None:
			if node.isLeftChild():
				node.parent.balanceFactor += 1
			elif node.isRightChild():
				node.parent.balanceFactor -= 1

			if node.parent.balanceFactor != 0:
				self.updateBalance(node.parent)


	def rebalance(self, node):

		if node.balanceFactor < 0:
			if node.rightChild.balanceFactor > 0:
				self.rotateRight(node.rightChild)
				self.rotateLeft(node)
			else:
				self.rotateLeft(node)
		elif node.balanceFactor > 0:
			if node.leftChild.balanceFactor < 0:
				self.rotateLeft(node.leftChild)
				self.rotateRight(node)
			else:
				self.rotateRight(node)


	def rotateRight(self, rotRoot):
		#define new root
		newRoot = rotRoot.leftChild
		#newroot left child becomes old root right child
		rotRoot.leftChild = newRoot.rightChild
		#Change child parent to match
		if newRoot.rightChild != None:
			newRoot.rightChild.parent = rotRoot
		#new root takes old roots parents
		newRoot.parent = rotRoot.parent
		#change root for tree
		if rotRoot.isRoot():
			self.root = newRoot
		#otherwise, change parents to match change
		else:
			if rotRoot.isRightChild():
				rotRoot.parent.rightChild = newRoot
			else:
				rotRoot.parent.leftChild = newRoot
		#old root is net roots left child
		newRoot.leftChild = rotRoot
		rotRoot.parent = newRoot
		rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
		newRoot.balanceFactor = newRoot.balanceFactor + 1 + min(rotRoot.balanceFactor, 0)

	def rotateLeft(self, rotRoot):

		#define new root
		newRoot = rotRoot.rightChild
		
		#newroot left child becomes old root right child
		rotRoot.rightChild = newRoot.leftChild
		
		#Change child parent to match
		if newRoot.leftChild != None:
			newRoot.leftChild.parent = rotRoot
		
		#new root takes old roots parents
		newRoot.parent = rotRoot.parent
		
		#change root for tree
		if rotRoot.isRoot():
			self.root = newRoot
		
		#otherwise, change parents to match change
		else:
			if rotRoot.isLeftChild():
				rotRoot.parent.leftChild = newRoot
			else:
				rotRoot.parent.rightChild = newRoot
		
		#old root is new roots left child
		newRoot.leftChild = rotRoot
		rotRoot.parent = newRoot
		rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
		newRoot.balanceFactor = newRoot.balanceFactor + 1 + min(rotRoot.balanceFactor, 0)



