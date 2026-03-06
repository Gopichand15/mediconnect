from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Hospital(request):
    return HttpResponse("This is Bhavani Branch")