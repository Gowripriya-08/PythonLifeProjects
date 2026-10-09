from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def demo(request):
    return render(request,'index.html')