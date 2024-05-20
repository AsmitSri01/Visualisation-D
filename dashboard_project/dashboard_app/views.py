from .models import Dashboard_data
from .serializers import Dashboard_Serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import JsonResponse
import json


# below code fetches data from the api
@api_view(['GET'])
def getdata(request):
    items = Dashboard_data.objects.all()
    serializer = Dashboard_Serializer(items, many=True)
    data = serializer.data
    return JsonResponse({'data': data}, safe=False)



def home(request):
     return render(request,'dashboard.html')





