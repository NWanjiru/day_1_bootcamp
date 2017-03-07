import unittest
from day_1_repo.prime_numbers import prime_numbers
class Test_Prime_Numbers(unittest.TestCase):
	"""Test whether prime_numbers() generates prime numbers"""

	def test_number_is_not_an_int(self):
		#Check if entered value is a string
		result = prime_numbers('mambo')
		self.assertEqual(result, 'This is not a number!')

	def test_number_is_not_greater_than_or_equal_to_one(self):
		#Check if entered value is greater than 1
		result = prime_numbers(3)
		self.assertNotEqual(result,[1])

	def test_number_is_divisible_by_2(self):
		#Check if entered value is even
		self.assertTrue(4%2 == 0,0)

	def test_it_does_not_generate_all_odd_numbers(self):
		#Check if when given a value, function generates all odd numbers in the range
		result = prime_numbers(5)
		self.assertEqual(result, [2,3,5])

	def test_the_generated_output_is_not_made_up_of_prime_numbers(self):
		#Check that the output lists only prime numbers
		""" 15 is divisible by 3 and 5, therefore not a prime number"""
		result = prime_numbers(15)
		self.assertFalse(result, [2, 3, 5, 7, 9, 11, 13, 15])