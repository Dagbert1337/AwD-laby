import math

def f(n, X):
	count = (1 + min(n, X-1)) / 2 * min(n, X-1)
	for i in range(2, min(n, math.isqrt(X-1))+1):
		# print(f"i: {i}, n: {n}, math: {math.isqrt(X-1)}  (+1)")
		for j in range(i, min(n, math.isqrt(X-1))+1):
			count += i*j
	count *= 2
	if math.sqrt(X)*math.sqrt(X) == X:
		count-=1
	return count

n = int(input())
X = int(input())

print(f(n, X))