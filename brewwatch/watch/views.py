from django.shortcuts import render
from django.http import HttpResponse
from models import Reading
import time
import json

# Create your views here.

def readings(request):
   return render(request, "watch/template/readings.html", {})
   
def registerReading(request):
    if request.method == 'POST':
        # get reading value from request
        reading_value = request.POST.get('reading')
        reading = Reading(value = reading_value, date = time.time())
        reading.save()
		
        return HttpResponse(status = 200)