#

from django.urls import path, include
from . import views

#
# from rest_framework import routers
#
# router = routers.DefaultRouter()
# router.register(r'dashboard',DashboardDatalist)
urlpatterns = [
    
    path('api/getdata/', views.getdata, name='getdata'),
    path('', views.home, name='home'),
]
