from django.shortcuts import render



from rest_framework.views import APIView
from rest_framework.response import Response
import rest_framework.status

import calendar
from datetime import datetime, timedelta
import traceback
import json

from . import models


class Uploader(APIView):
   # Create your views here.
   def post (self, request):
        post_data = dict(request.data)
        serialised_post_data = models.CheckInPhotoDBSerializer(data=post_data, partial=True)
        if serialised_post_data.is_valid():
            obj = models.CheckinPhotoDB.create(**serialised_post_data.data)
            return Response(True, status=201)
        else: 
            return Response(False, status=500)

       

class Reader(APIView):
   # Create your views here.
   def post (self, request):
       post_data = dict(request.data)
       
        try:
           if post_data.has_key("email"):
                obj = models.CheckinPhotoDB.filter(Email=post_data["email"])
                 
            elif post_data.has_key("mobile"):
                obj = models.CheckinPhotoDB.filter(Mobile=post_data["mobile"])
                
            elif post_data.has_key("user_id"):
                obj = models.CheckinPhotoDB.filter(Userid=post_data["user_id"])

            serialised_data = models.CheckInPhotoDBSerializer(obj, many=True)
            return Response (
                    serialised_data.data, 
                    status=201,
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
                obj = models.CheckinPhotoDB.delete(Email=post_data["email"])
                 
            elif post_data.has_key("mobile"):
                obj = models.CheckinPhotoDB.delete(Mobile=post_data["mobile"])
                
            elif post_data.has_key("user_id"):
                obj = models.CheckinPhotoDB.delete(Userid=post_data["user_id"])

            elif post_data.has_key("img_url"):
                obj = models.CheckinPhotoDB.delete(AWSPhotoUrl=post_data["img_url"])

            return Response (True, status=201)

        except Exception, e:
            ## 404
            return Response(False, status=500)



 