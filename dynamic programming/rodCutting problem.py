price = [0, 1, 5, 8, 9, 10, 14, 17, 20, 24, 30]
cut_point = []

def cut_rod(length):
	if length <= 0:
		return 0
	print (price)
	cut_point.append(0)
	for i in range(1,length+1):
		result = price[i]
		cut_point.append(0)
		for j in range(1,i+1):
			if result < (price[j] + price[i-j]):
				result = price[j] + price[i-j]
				cut_point[i] = j
				price[i] = result
	print("cut point:",cut_point)
	print("price:",price)

def recursiveCut(start, length):
	cut = cut_point[length]
	if cut == 0:
		return
	recursiveCut(start, cut)
	print(cut + start)
	recursiveCut(cut, length - cut)

def getCutRodPlan(length):
	cut_rod(length)
	print("cut plan:")
	recursiveCut(0, length)

getCutRodPlan(8)