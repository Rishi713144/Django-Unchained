from django.shortcuts import render, get_object_or_404
from .forms import newappForm
from .models import newappmodel


def home(request):
    return render(request, 'website/index.html')


def all_newapp(request):
    items = newappmodel.objects.all()
    return render(request, 'newapp/all_newapp.html', {
        'items': items
    })


def newapp_detail(request, newapp_id):
    newapp = get_object_or_404(newappmodel, pk=newapp_id)
    return render(request, 'newapp/newapp_detail.html', {
        'newapp': newapp
    })


def newapp_stories(request):
    stories = newappmodel.objects.all()
    form = newappForm()

    if request.method == 'POST':
        form = newappForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'newapp/newapp_stories.html', {
        'stories': stories,
        'form': form
    })
