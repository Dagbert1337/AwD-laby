def suma_malych_iloczynow(tab, K):
	sum=0
	for i in range(len(tab) - 1):
		for j in range(i+1 ,len(tab)):
			if tab[i]*tab[j] < K:
				sum+=tab[i]*tab[j]
	return sum

n = int(input())
tab = [int(input()) for _ in range(n)]
K = int(input())

print(suma_malych_iloczynow(tab, K))