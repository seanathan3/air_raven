from django.shortcuts import render
from django.http import HttpResponse
from .models import Flight
# Create your views here.

def index(request):
    flights = Flight.objects.all()
    return render(request, "app/index.html", {"flights": flights})