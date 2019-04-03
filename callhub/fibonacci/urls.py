import fibonacci.views as views

from django.urls import include, path, re_path

app_name = 'fibonacci'

urlpatterns = [
	
	path('', 
		views.HomePage.as_view(),
		 name='homepage'),
]