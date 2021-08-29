from django.urls import path

from . import views

urlpatterns = [
    path('', views.test_vue, name='test_vue'),
]