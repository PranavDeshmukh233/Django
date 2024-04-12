from django.urls import path
from . import views

urlpatterns =[
    path('Home/',views.homeview.as_view()),
    path('Authorize/',views.Authorize.as_view())

]
