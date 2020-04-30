from .algorithm import Algorithm

class SortAlgorithm(Algorithm):
	def __init__(self):
		super().__init__()
		self._type = "sort"

class BubbleSortAlgorithm(SortAlgorithm):
	def __init__(self):
		super().__init__()
		self.setName("Bubble_Sort")

	def execute(self, numberList):
		exchanges = True
		lengthOfList = len(numberList)-1
		while lengthOfList > 0 and exchanges:
			exchanges = False
			
			for i in range(lengthOfList):
				if numberList[i] > numberList[i+1]:

					#Identify
					yield numberList, [[i], [i+1]], "Identified"

					#Swap
					exchanges = True
					temp = numberList[i]
					numberList[i] = numberList[i+1]
					numberList[i+1] = temp
					
					#Return Result
					yield numberList, [[i], [i+1]], "Swapped"

class InsertSortAlgorithm(SortAlgorithm):
	def __init__(self):
		super().__init__()
		self.setName("Insert_Sort")

	def execute(self, numberList):
		for index in range(len(numberList)):
			current_value = numberList[index]			
			
			while (index > 0 and numberList[index-1] > current_value):

				#Identify
				yield numberList, [[index], [index-1]], "Identified"
				
				#Swap
				numberList[index] = numberList[index-1]
				numberList[index-1] = current_value

				#Return
				yield numberList, [[index-1], [index]], "Swapped"
				index -= 1


class SelectionSortAlgorithm(SortAlgorithm):
	def __init__(self):
		super().__init__()
		self.setName("Selection_Sort")

	def execute(self, numberList):
		for spot in range(len(numberList)-1, 0, -1):
			maxLocation = 0
			for i in range(1, spot+1):
				if numberList[i] > numberList[maxLocation]:
					maxLocation = i
			
			yield numberList, [[maxLocation], [spot]], "Identified"

			temp = numberList[spot]
			numberList[spot] = numberList[maxLocation]
			numberList[maxLocation] = temp
		
			yield numberList, [[maxLocation], [spot]], "Swapped"


class MergeSortAlgorithm(SortAlgorithm):
	def __init__(self):
		super().__init__()
		self.setName("Merge_Sort")

	def execute(self, numberList, changedList=None):
		#Func's needs option to be passed alist
		if changedList == None:
			changedList = numberList
		
		if len(changedList) > 1:

			#splitting into two lists
			split = len(changedList)//2

			firstIndexed = list(range(split))
			secondIndexed = list(range(split, len(changedList)))
			
			first = changedList[:split]
			second = changedList[split:]

			yield numberList, [firstIndexed, secondIndexed], "Split"

			#splitting until individual numbered lists
			yield from self.execute(numberList, first)
			yield from self.execute(numberList, second)

			#Sort smallest to largest
			i=0
			j=0
			k=0

			first_lower = False

			start = numberList.index((first + second)[0])
			length = len(changedList)

			while i < len(first) and j < len(second):
				if first[i] <= second[j]:
					changedList[k] = first[i]
					i+=1
					first_lower = True
				else:
					changedList[k] = second[j]
					j+=1
				k+=1

			while i < len(first):
				changedList[k] = first[i]
				i+=1
				k+=1

			while j < len(second):
				changedList[k] = second[j]
				j+=1
				k+=1

			for i in range(length):
				numberList[start] = changedList[i]
				start += 1

			#returns changed displays
			if first_lower:
				merge = numberList, [firstIndexed, secondIndexed]
			else:
				merge = numberList, [secondIndexed, firstIndexed]

			yield merge, "Sorted"

		else:
			pass


class ShellSortAlgorithm(SortAlgorithm):
	def __init__(self):
		super().__init__()
		self.setName("Shell_Sort")

	def execute(self, numberList):
		#Define Variables
		if numberList == None:
			numberList = numberList

		gap = len(numberList)//2

		#Iterate Trhough Sublists
		while gap > 0:

			#Iterate Through Start Positions Per SubList
			for startposition in range(gap):
				
				#Define Sublist
				sublist = [startposition]
				while startposition + gap < len(numberList):
					sublist.append(startposition + gap)
					startposition = startposition + gap

				#Perform Insert Sort In SubList
				for index in range(len(sublist)):

					current_value = numberList[sublist[index]]

					while index > 0 and numberList[sublist[index-1]] > current_value:

						#Identify
						yield numberList, [[sublist[index]], [sublist[index-1]]], "Identified"

						#Swap
						numberList[sublist[index]] = numberList[sublist[index-1]]
						numberList[sublist[index-1]] = current_value

						#Return
						yield numberList, [[sublist[index-1]], [sublist[index]]], "Swapped"
						index -= 1

			gap = gap // 2



class QuickSortAlgorithm(SortAlgorithm):
	def __init__(self):
		super().__init__()
		self.setName("Quick_Sort")

	def execute(self, numberList, first=0, last=None):
		if last == None:
			last = len(numberList)-1
		
		if first < last:

			splitpoint = yield from self.partition(numberList, first, last)

			yield from self.execute(numberList, first, splitpoint-1)
			yield from self.execute(numberList, splitpoint+1, last)


	def partition(self, numberList, first, last):

		pivotvalue = numberList[first]

		leftmark = first+1
		rightmark = last

		done = False
				
		while not done:

			while leftmark <= rightmark and numberList[leftmark] <= pivotvalue:
				leftmark = leftmark + 1

			while rightmark >= leftmark and numberList[rightmark] >= pivotvalue:
				rightmark = rightmark - 1

			if rightmark < leftmark:
				done = True
			else:
				yield numberList, [[leftmark], [rightmark], [first]], "Identified"
			
				temp = numberList[leftmark]
				numberList[leftmark] = numberList[rightmark]
				numberList[rightmark] = temp

				yield numberList, [[leftmark], [rightmark], [first]], "Swapped"

		# yield [numberList, [first], [rightmark], [first, rightmark]]

		temp = numberList[first]
		numberList[first] = numberList[rightmark]
		numberList[rightmark] = temp

		yield numberList, [[first], [rightmark], [rightmark, first]], "Pivot Change"
		
		return rightmark

