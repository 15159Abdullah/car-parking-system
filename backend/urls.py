
from django.urls import path
from backend import views

 
urlpatterns = [
   
    path('index/',views.index,name='index'),

    #__________________User Url________________________
    path('user_list/',views.user_list,name='user_list'),
    path('delete_user/<pk>/',views.delete_user,name='delete_user'),
 
    #__________________Contact Url________________________
    path('contact_list/',views.contact_list,name='contact_list'),
    path('delete_contact/<pk>/',views.delete_contact,name='delete_contact'),

    #__________________Slots Url________________________
    path('checked/<pk>/',views.checked,name='checked'),
    path('slots_list/',views.slots_list,name='slots_list'),
    path('add_slot/',views.add_slot,name='add_slot'),
    path('update_slot/<pk>/',views.update_slot,name='update_slot'),
    path('delete_slot/<pk>/',views.delete_slot,name='delete_slot'),
    path('slots_request/',views.slots_request,name='slots_request'),
    path('delete_slots_request/<pk>/',views.delete_slots_request,name='delete_slots_request'),
    path('confirm_slot/<pk>/',views.confirm_slot,name='confirm_slot'),

    #__________________Area Url________________________
    path('area_list/',views.area_list,name='area_list'),
    path('add_area/',views.add_area,name='add_area'),
    path('update_area/<pk>/',views.update_area,name='update_area'),
    path('delete_area/<pk>/',views.delete_area,name='delete_area'),
 

    #__________________Parking Url________________________
    path('parking_list/',views.parking_list,name='parking_list'),
    path('add_parking/',views.add_parking,name='add_parking'),
    path('update_parking/<pk>/',views.update_parking,name='update_parking'),
    path('delete_parking/<pk>/',views.delete_parking,name='delete_parking'),


    #__________________Invoice____________________________

    path('invoice/<pk>/',views.invoice,name='invoice'),
   
] 