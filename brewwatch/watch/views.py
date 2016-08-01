from django.shortcuts import render
from django.http import HttpResponse
from models import Reading
import time
from django.core import serializers

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
		
def readingData(request):
    if request.method == 'GET':
        all = Reading.objects.all()

        json_serializer = serializers.get_serializer("json")()
        response =  json_serializer.serialize(all, ensure_ascii=False, indent=4)
        return HttpResponse(response)