from django.urls import path, include 
from . import views 
app_name = 'authentication_app'
urlpatterns = [
     path('countries/', views.country_list, name='country_list'),
     path('countries/<int:pk>/edit/', views.country_edit, name='country_edit'),
]
#urlpatterns = [
#    path("", views.index, name="index"),  
#]
#urlpatterns = [ 
#    path("", views.country, name="country"), 
#]
#urlpatterns = [
#    path("", views.city, name="city"),  
#]