from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	path('', views.post_list, name = 'post_list'),
] + static(settings.STATIC_URL, documnet_root=settings.STATIC_URL)
