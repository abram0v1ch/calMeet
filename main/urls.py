from django.urls import path
from . import views

urlpatterns = [
    path('join/<code>/', views.main),
    path('new_room/', views.new_room),
    path('new_user/', views.new_user),
    path('get_times/', views.get_times),
]