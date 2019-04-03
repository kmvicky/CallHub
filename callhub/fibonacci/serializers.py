from rest_framework import serializers

class FibonacciNthNumberSerializer(serializers.Serializer):

	number 					= serializers.IntegerField()
	fibonacci_nth_number 	= serializers.IntegerField()