from django.shortcuts import render



from rest_framework.views import APIView
from rest_framework.response import Response
import rest_framework.status

import calendar
from datetime import datetime, timedelta
import traceback
import json
import requests


from .models import *


class Uploader(APIView):
   # Create your views here.
   def post (self, request):
        #import pdb;pdb.set_trace()
        post_data = dict(request.data)
        print post_data
        serialised_post_data = CheckInPhotoDBSerializer(data=post_data, partial=True)
        if serialised_post_data.is_valid():
            try:
               # check image is valid
               result = ocr_space_url(url=serialised_post_data.data["AWSPhotoUrl"])
               result_json = json.loads(result)
               if not result_json["IsErroredOnProcessing"] or result_json["OCRExitCode"]!=1 or len(result_json["ParsedResults"])<1 or len(result_json["ParsedResults"][0]["ParsedText"])<2:
                 return Response({"is_valid":False}, status=400)

               obj = CheckInPhotoDB.objects.create(**serialised_post_data.data)
            except Exception, e:
                print e
                return Response({"is_valid":False}, status=500)
            return Response({"is_valid":True}, status=200)
        else: 
            return Response({"is_valid":False}, status=500)

       

class Reader(APIView):
   # Create your views here.
   def get (self, request):
        post_data = dict(request.GET.dict())
       
        try:
            if post_data.has_key("email"):
                 obj = CheckInPhotoDB.objects.filter(Email=post_data["email"])
                 
            elif post_data.has_key("mobile"):
                obj = CheckInPhotoDB.objects.filter(Mobile=post_data["mobile"])
                
            elif post_data.has_key("user_id"):
                obj = CheckInPhotoDB.objects.filter(Userid=post_data["user_id"])

            serialised_data = CheckInPhotoDBSerializer(obj, many=True)
            return Response (
                    serialised_data.data, 
                    status=200,
                    )

        except Exception, e:
            ## 404
            return Response({}, status=404)




class Updater(APIView):
   # Create your views here.
   def post (self, request):
        return Response({}, status=201)

class Deleter(APIView):
   # Create your views here.
   def post (self, request):
        post_data = dict(request.data)
       
        try:
            if post_data.has_key("email"):
                obj = CheckInPhotoDB.objects.delete(Email=post_data["email"])
                 
            elif post_data.has_key("mobile"):
                obj = CheckInPhotoDB.objects.delete(Mobile=post_data["mobile"])
                
            elif post_data.has_key("user_id"):
                obj = CheckInPhotoDB.objects.delete(Userid=post_data["user_id"])

            elif post_data.has_key("img_url"):
                obj = CheckInPhotoDB.objects.delete(AWSPhotoUrl=post_data["img_url"])

            return Response (True, status=201)

        except Exception, e:
            ## 404
            return Response(False, status=500)




def ocr_space_url(url, overlay=False, api_key='d33a8c2d0e88957', language='eng'):
    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return r.content

test_url = ocr_space_url(url='https://s11.postimg.org/61bp61czn/IMG_20161010_201926.jpg')
# print test_url
d = json.loads(test_url)
 