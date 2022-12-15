from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from datetime import datetime  #used to import date and time (inbuild in django)


# Create your views here.

class indexview(View):
    def get(self,request):
        current_time=datetime.now() # now is 
        html="<html><body>Current date and time is{}</body></html>".format(current_time)
        return HttpResponse(html)