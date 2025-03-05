def binarySearch(data,item):
	low = 0
	high = len(data)-1
	pos = -1
	while low <= high and pos == -1:
		mid = (low + high) // 2
	if item > data[mid]:
		low = mid + 1
	elif item < data[mid]:
		high = mid - 1
	else:
		return mid
	return -1
result = binarySearch([1,3,4,15,18,20,24,28],4)
print(result)
result1 = binarySearch([1,3,4,15,18,20,24,28],99)
print(result1)

