from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    context = {
        "tv_shows_list": Show.objects.all()
    }
    return render(request, 'tv_shows/index.html', context)

def show_details(request, show_id):
    context = {
        'tv_show': Show.objects.get(id=show_id)
    }
    return render(request, 'tv_shows/details.html', context)

def show_edit(request, show_id):
    if request.method == "GET":    
        context = {
            "tv_show": Show.objects.get(id=show_id),
            "networks": Network.objects.all()
        }
        
        return render(request, 'tv_shows/edit.html', context)

    else:
        tv_show = Show.objects.get(id=show_id)
        tv_show.title = request.POST['title']
        tv_show.network = Network.objects.get(id=request.POST['network'])
        tv_show.release_date = request.POST['released']
        tv_show.description = request.POST['desc']
        tv_show.save()
        return redirect(f'/shows/{show_id}')

def show_delete(request, show_id):
    to_delete = Show.objects.get(id=show_id)
    to_delete.delete()
    return redirect('/')

def show_new(request):
    if request.method == "POST":
        Show.objects.create(title=request.POST['title'], release_date=request.POST['released'], description=request.POST['desc'], network=Network.objects.get(id=request.POST['network']))
        return redirect('/shows')

    context = {
        "networks": Network.objects.all()
    }
    return render(request, 'tv_shows/add.html', context)
