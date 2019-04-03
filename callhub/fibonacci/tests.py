from django.test import TestCase
from callhub.fibonacci.models import *

class FibonacciTestCase(TestCase):

	def setUp(self):
		FibonacciNthNumber.objects.create(number=21, fibonacci_nth_number=10946)
		FibonacciNthNumber.objects.create(number=12, fibonacci_nth_number=144)

	def test_fibonacci(self):
		try:
			fibonacci_number_12 = FibonacciNthNumber.objects.get(number=12)
			self.assertEqual(fibonacci_number_12.fibonacci_nth_number, 144)
		except Exception as e:
			count=1
			current=1
			prev=0
			while count < int(12):
				current, prev = current + prev, current
				count = count + 1

			fibonacci_number_12 = FibonacciNthNumber.objects.create(number=12, fibonacci_nth_number=current)

			self.assertEqual(fibonacci_number_12.fibonacci_nth_number, 144)