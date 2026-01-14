import math

def sumy_kwadratow(k, p):
	if math.isnan(k) or math.isnan(p) or p<k:
		print("error")
		return
	answers = [0]*(p-k+1)
	
	for i in range(1, math.isqrt(p//2)):
		if k>i**2:
			for j in range(math.isqrt(k-i**2), math.isqrt(p-i**2)+1):
				if answers[i**2 + j**2 - k] == 0 and i != j:
					answers[i**2 + j**2 - k] = 1
					print(i**2 + j**2)
		else:
			for j in range(1, math.isqrt(p-i**2)+1):
				if answers[i**2 + j**2 - k] == 0 and i != j:
					answers[i**2 + j**2 - k] = 1
					print(i**2 + j**2)		

# k = int(input())
# p = int(input())
sumy_kwadratow(1, 20)