class HashTable():
	def __init__(self):
		self.size = 11
		self.slots = self.size * [None]
		self.data = self.size * [None]

	def get(self, key):
		found = False
		stop = False
		data = False
		hashed_value = self.hash(key)
		position = hashed_value
		while not found and not stop and self.slots[position] != None:
			if self.slots[position] == key:
				found = True
				data = self.data[position]
			else:
				position = self.rehash(position)
				if position == hashed_value:
					stop = True

		return data

	def put(self, key, data):
		print(f"entered put, {key}, {data}")
		hashed_value = self.hash(key)
		print(f"hashed value: {hashed_value}")

		while self.slots[hashed_value] != None:
			print(f"slots hashed value: {self.slots[hashed_value]}")
			print(self.slots)

			if self.slots[hashed_value] == key:
				self.data[hashed_value] = data
			else:
				hashed_value = self.rehash(hashed_value)

		self.slots[hashed_value] = key
		self.data[hashed_value] = data
		print(f"Done Put, {key, {data}}")

	def hash(self, key):
		hashed_value = key%11
		return hashed_value

	def rehash(self, hashed_value):
		last_slot = len(self.slots)-1
		if hashed_value == last_slot:
			hashed_value = 0
		else:
			hashed_value += 1
		return hashed_value

	def inputList(self, alist):
		self.setSize(alist)
		for index, number in enumerate(alist):
			print(index, number)
			self.put(number, index)

	def setSize(self, alist):
		length = len(alist)
		if length <= 11:
			self.size = 11
		elif length <= 23:
			self.size = 23
		else:
			self.size = 53

	def __getitem__(self, key):
		return self.get(key)

	def __setitem__(self, key, data):
		return self.put(key, data)

	def showKeys(self):
		return print(self.slots)

	def showData(self):
		return print(self.data)

	def __contains__(self, item):
		return self.get(item)
