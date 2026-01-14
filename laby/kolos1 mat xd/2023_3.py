def search_similar_patterns(t, w, k):
	matches = 0
	ans = [0] * len(t)
	i = 0
	t_end = len(t)
	w_end = len(w)
	while i < t_end - w_end + 1:
		k_left = k
		
		for j in range(w_end):
			if t[i+j] != w[j]:
				k_left -= 1
				
		if k_left >= 0:
			ans[matches] = i
			matches += 1
		
		i += 1

	f_ans = [ans[g] for g in range(matches)]
	
	return f_ans

t = [1, 2, 3, 5, 2, 3, 4, 5, 3, 1, 3, 5]
w = [2, 3, 5]

print(search_similar_patterns(t, w, 1))
print(search_similar_patterns(t, w, 2))
print(search_similar_patterns(t, [1, 1, 1, 1], 0))