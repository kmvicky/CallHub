import time
from django.urls import reverse
from callhub.fibonacci.models import *
from django.views.generic import View, TemplateView
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseNotFound



class HomePage(TemplateView):

	def get(self, request, *args, **kwrgs):

		self.template_name = 'fibonacci/fibonacci.html'
		
		try:
			context = {
				'action': reverse('fibonacci:homepage')
			}

			return self.render_to_response(context)

		except Exception as e:
			raise e


	def post(self, request, *args, **kwrgs):

		self.template_name = 'fibonacci/fibonacci.html'
		
		try:
			start = time.time()
			
			data = request.POST.dict()

			number = data.get('number', None)

			try:
				fibonacci_sequence_number = FibonacciNthNumber.objects.get(number=int(number))
			except:
				count=1
				current=1
				prev=0
				while count < int(number):
					current, prev = current + prev, current
					count = count + 1

				params = {
					'number': number,
					'fibonacci_nth_number': current
				}
				
				fibonacci_sequence_number = FibonacciNthNumber.objects.create(**params)

			end = time.time()

			context = {
				'time': end - start,
				'number': fibonacci_sequence_number.fibonacci_nth_number
			}

			return JsonResponse(context)
		
		except Exception as e:
			return HttpResponseNotFound(str(e))