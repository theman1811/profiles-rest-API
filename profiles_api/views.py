from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """TEST API VIEW"""
    
    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview= [
            "Uses HTTP methods as function (get, post, put, patch, delete)",
            "Is similar to a traditional Django View",
            "Gives you the most control over you application logic",
            "Is mapped mannually to Urls"
        ]

        return Response({"message": 'Hello', "an_apiview": an_apiview})
