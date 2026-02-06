from django.shortcuts import render
from .models import newappmodel
from django.shortcuts import get_object_or_404
def all_newapp(request):
    items = newappmodel.objects.all()
    return render(request, 'newapp/all_newapp.html', {'items': items})

def home(request):
    return render(request, 'website/index.html')

def newapp_detail(request, newapp_id):
    newapp=get_object_or_404(newappmodel, pk=newapp_id)
    return render(request, 'newapp/newapp_detail.html', {'newapp': newapp})