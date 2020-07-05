from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("<h1>hello world</h1>");
    return render(request, 'index1.html',{'name':'abhishek'})


def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2']) 
    res = val1 + val2

    return render(request, 'result.html', {'result':res}) 
