from django.shortcuts import render
from  django.http import HttpResponse
from .models import Place,Basket
# Create your views here.


def demo(request):
    obj = Place.objects.all()
    obj2 = Basket.objects.all()

    return render(request, "index.html", {'result': obj,'result2':obj2})


#def about(request):
   # return render(request, "about.html")


#def content(request):
   # return HttpResponse('hello i am content')


#def addition(request):
 #   value1 = int(request.GET['num1'])
  #  value2 = int(request.GET['num2'])
  #  result = value1 + value2
   # return render(request, "about.html", {"res":result})
