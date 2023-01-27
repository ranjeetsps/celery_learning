from . import views
from .views import detail
from django.urls import path

urlpatterns = [
  path('detail', detail.as_view(), name='home'),
]  
