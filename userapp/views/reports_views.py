from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def reports(request):
    return HttpResponse("<h1>Welcome to Reports</h1>")
