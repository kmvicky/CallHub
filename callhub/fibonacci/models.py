from django.db import models

class FibonacciNthNumber(models.Model):

	number 					= models.PositiveIntegerField()
	fibonacci_nth_number 	= models.BigIntegerField()

	def __str__(self):
		return '{}->{}'.format(self.number, self.fibonacci_nth_number)