from django.shortcuts import render

# Create your views here.

def readings(request):
   return render(request, "watch/template/readings.html", {})