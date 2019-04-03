import fibonacci.views as views

from django.urls import include, path, re_path
from django.conf.urls.static import static

app_name = 'fibonacci'

urlpatterns = [
	
	path('', 
		views.HomePage.as_view(),
		 name='homepage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)