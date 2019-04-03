from django.apps import AppConfig

class FibonacciConfig(AppConfig):

	name = 'callhub.fibonacci'
	verbose_name = 'fibonacci'

	def ready(self):
		pass