from django.shortcuts import render
from .models import MyImage
# Create your views here.
def home(request):
    images =MyImage.objects.all()
    context = {
        'images':images
    }
    return render(request,'index.html',context)
