from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'newapp/all_newapp.html')

def all_newapp(request):
    return render(request, 'newapp/all_newapp.html') 