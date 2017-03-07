def prime_numbers(n):
	#Check whether n is a prime number 
	#Generate a list of prime numbers between 0 and n
	prime = []
	if type(n) is int:
		#Check if the element n is an integer
		for i in range(1,n+1):
			if i <=1:
				pass
			elif i == 2 or i % 2 != 0:
				prime.append(i)
		return prime
	else:
		return 'This is not a number!'
