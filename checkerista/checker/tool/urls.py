from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'^results/$',views.results, name ='results'),

   # path('/result/',views.result, name='result'),
]