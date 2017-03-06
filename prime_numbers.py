def prime_numbers(n):
	if isinstance(n, int):
		if n ==2 or n % 2 != 0:
			return (n)
	else:
		return 'This is not a number!'
