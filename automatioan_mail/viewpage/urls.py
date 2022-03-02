from django.urls import path
from . import views
urlpatterns=[
path('',views.view,name='my_page'),
path('Ajax',views.submet_email,name ='Ajax'),
path('Contact_Us',views.Contact_Us,name='Contact_Us'),
 
 ]
