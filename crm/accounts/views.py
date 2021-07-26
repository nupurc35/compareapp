from django.shortcuts import render, redirect 
from django.http import HttpResponse,JsonResponse
from .models import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from rest_framework import routers, serializers, viewsets
from .serializers import smartPhoneSerializer
from django.template import loader 
# Create your views here.

class smartPhoneViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """
    queryset = smartPhone.objects.all()
    serializer_class = smartPhoneSerializer

"""
def alldetails(request):
     
      allSmartphones = smartPhone.objects.all()
      
      context = {'allSmartphones':allSmartphones}
      
      return render(request, 'accounts/dash.html',context)
"""   
def index(request):
        """
        smartPhone = smartPhone.objects.all()
      
        context    = {'smartPhone':smartPhone}
      
        return render(request, 'compareapp/index.html',context)      # rendering the template in HttpResponse  
        """
        allSmartphones = smartPhone.objects.all()
      
        #context = {'allSmartphones':allSmartphones}
        template =loader.get_template('compareapp/dashboard.html') 
        context = {
               'allsmartPhones':allSmartphones 
        }
        return HttpResponse(template.render(context,request))