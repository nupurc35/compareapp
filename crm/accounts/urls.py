from django.urls import path,include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'smartPhones', views.smartPhoneViewSet)
urlpatterns = [
     path('', include(router.urls)),
     path('hello/',views.index,name="hello") 
]

