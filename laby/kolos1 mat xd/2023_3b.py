def g(x, n):
	up = 1
	down = 1
	sum = 0

	for i in range(1, n+2):
		up *= (-8 * x * x)
		down *= 2 * i * (2 * i + 1)
		sum += up/down
	
	sum += 4 * x
	
	return sum

print (g(3, 2))