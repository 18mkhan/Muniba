def bubbleSort(data):
	swap = True 
	while swap == True:
		I = 0
		swap = False
		while i < len(data) -1:
			if data[i] > data[i+1]:
				temp = data[i]
				data[i] = data[i+1]
				data[i+1] = temp
				swap = True 
			i+=1
