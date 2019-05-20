array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

def twoNumberSum(array, targetSum):
    
	startIndex = 0
	endIndex = len(array) - 1
	
	for index in range(startIndex, endIndex):
		for i in range(0, index):
			if array[index] + array[i] == targetSum:
				if array[index] < array[i]:
					return [array[index], array[i]]
				else:
					return [array[i], array[index]]
		for j in range(index, endIndex + 1):
			if array[index] + array[j] == targetSum:
				if array[index] < array[j]:
					return [array[index], array[j]]
				else:
					return [array[j], array[index]]
	
	return []

result = twoNumberSum(array, targetSum)
print(result)