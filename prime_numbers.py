def prime_numbers(n):
	prime = []
	if isinstance(n, int):
		for i in range(1,n+1):
			if i <=1:
				pass
			elif i == 2 or i % 2 != 0:
				prime.append(i)
		return prime
	else:
		return 'This is not a number!'
