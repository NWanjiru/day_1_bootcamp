def prime_numbers(n):
	prime = []
	if isinstance(n, int):
		if n ==2 or n % 2 != 0:
			for i in range(n):
				j = i - 1
				if i % j != 0:
					prime.append(i)
				j -= 1

			return prime
	else:
		return 'This is not a number!'
