from django.urls import path
from .views import*

urlpatterns =[
     path('',home,name='home'),
     path('about/',about,name='about'),
     path('doctor/',doctor,name='doctor'),
     path('department/',department,name='department'),
     path('contact/',contact,name='contact'),
     path('booking/',booking,name='booking'),
     path('confirm/',booking,name='confirm'),

]
