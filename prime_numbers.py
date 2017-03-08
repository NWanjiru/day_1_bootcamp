def prime_numbers(n):
	"""Generate a list of prime numbers between 0 and n"""
	prime = []
	if type(n) is int:
		#Check if the element n is an integer
		for i in range(1,n+1):
			if i <=1:
				pass
			elif i == 2 or i % 2 != 0:
				if i <= 3 or i % 3 != 0:
					if i <= 5 or i % 5 !=0:
						if i <= 7 or i % 7 !=0:
							prime.append(i)
		return prime
	else:
		return 'This is not a number!'
