from django.shortcuts import render
from django.http import HttpResponse

# def demo(request):
#     return render(request, 'index.html')

# Create your views here.
def calculator(request):
    solution = ''
    if request.method =='POST':
        a =float( request.POST.get('a'))
        b = float(request.POST.get('b'))
        opr = request.POST.get("opr")
        if opr =='+':
            solution = a+b
        elif opr =='-':
            solution = a-b
        elif opr =='*':
            solution = a*b
        elif opr == '/':
            solution = a/b
        elif opr =='**':
          solution = a**b
        else:
            solution = "invalid output"

    return render(request,'index.html',{"solution":solution})