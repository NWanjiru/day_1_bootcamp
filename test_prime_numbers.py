import unittest
from day_1_repo.prime_numbers import prime_numbers
class Test_Prime_Numbers(unittest.TestCase):

	def test_if_number_is_not_an_int(self):
		result = prime_numbers('mambo')
		self.assertEqual(result, 'This is not a number!')

	def test_if_number_is_divisible_by_2(self):
		self.assertTrue(4%2 == 0,0)

	def test_if_number_is_not_equal_to_two(self):
		self.assertNotEqual(7,2)

