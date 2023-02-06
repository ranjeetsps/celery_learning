from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.tasks import mul
# Create your views here.

class detail(APIView):
    def get(self,request):
        print("get caught")
        try:
            c= 'hi this is for celery testing'
            message= 'hii welcome this for celery testing'
            task = mul
            mul.delay(2,3)
            print("returning response")
            return Response({'status':200,'message':message})
        except Exception as e:
            return Response({'status':500,'message':str(e)})    
