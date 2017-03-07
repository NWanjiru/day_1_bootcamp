import unittest
from day_1_repo.prime_numbers import prime_numbers
class Test_Prime_Numbers(unittest.TestCase):
	#Test whether prime_numbers() generates prime numbers

	def test_if_number_is_not_an_int(self):
		#Test if entered value is a string
		result = prime_numbers('mambo')
		self.assertEqual(result, 'This is not a number!')

	def test_if_number_is_not_greater_than_or_equal_to_one(self):
		#Test if entered value is greater than 1
		result = prime_numbers(3)
		self.assertNotEqual(result,[1])

	def test_if_number_is_divisible_by_2(self):
		#Test if entered value is even
		self.assertTrue(4%2 == 0,0)

	def test_if_number_is_not_equal_to_two(self):
		#Test if entered value is not two. 
		#Two is a prime number
		self.assertNotEqual(7,2)

	def test_if_it_does_not_generate_all_odd_numbers(self):
		#Test if when given a value, function generates all odd numbers in the range
		result = prime_numbers(5)
		self.assertEqual(result, [2,3,5])