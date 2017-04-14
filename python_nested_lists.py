marks = [4,6,8,7,23,2.5, 1]
marks2 = [6,4,45,68,23]
marks3 = [2, 34, 1, 2, 88]
marks4 = [1,1,2,2,34,56]
marks5 = [2,2,1,1,34,56]
marks6 = [1,1,1,1,1,1]
def least_two(marks):
	least = marks[0]
	y = 1
	while y<len(marks):
		if marks[y] == least:
			#print(marks[y])
			y+=1
		else:
			break
	if y == len(marks):
		raise ValueError('All elements in the given list are equal')
	second_least = marks[y]	
	if least > second_least:
		a = least
		least = second_least
		second_least = a
	x = y+1
	while x<len(marks):
		#print('enterd while')
		if marks[x] < second_least:
			if marks[x] > least:
				second_least = marks[x]
			elif marks[x] < least:
				second_least = least
				least = marks[x]
		x+=1
				
	return least, second_least
	
if __name__ == '__main__':
	print(least_two(marks))
	print(least_two(marks2))			
	print(least_two(marks3))		
	print(least_two(marks4))
	print(least_two(marks5))
	print(least_two(marks6))			
		
	