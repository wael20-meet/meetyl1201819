def exercise01(x):
	z = x[0]
	y = x[4]
	list01 = [z,y]
	return list01


list02 = [1,2,3,4,5]

exercise01 (list02)
list01 = exercise01(list02)
print(list01)

c = [1,2,4,3,5,23,29,55,68,79]

def ex02(l):
	for i in l:
		if i < 5:  
			print(i)
ex02(c)


def is_prime(a):
	print(a)
	if (a%2) == 0:
		return False
	for i in range(2,a):
		if a//i == type(int):
			return True
	return 'car'
print(is_prime(13))
