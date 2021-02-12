from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    about = About.objects.first()
    services = Service.objects.all()
    porfolio = Portfolio.objects.all()
    blog = Blog.objects.all()
    return render(request,'index.html',{'about':about,'service':services,'work':porfolio,'blog':blog})