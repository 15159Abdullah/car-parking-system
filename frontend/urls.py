

from django.urls import path
from frontend import views

urlpatterns = [
   
    path('home/',views.index,name='home'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('slots/<pk>/',views.slots, name='slots'),
    path('parking/',views.parking, name='parking'),
    path('search_parking/',views.search_parking, name='search_parking'),
    path('slot_order/',views.slot_order, name='slot_order'),
    path('booked/<pk>/',views.booked, name='booked'),
    path('profile/<pk>/',views.profile, name='profile'),
]