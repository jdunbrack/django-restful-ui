from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

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
        errors = Show.objects.basic_validator(request.POST)

        title_test = Show.objects.filter(title=request.POST['title']).exclude(id=show_id)
        if len(title_test) > 0:
            messages.error(request, "Show with this title already exists. Choose another title.")
            return redirect(f'/shows/{show_id}/edit')

        if len(errors) > 0:
            for value in errors.values():
                messages.error(request, value)
            return redirect(f'/shows/{show_id}/edit')
        
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

        title_test = Show.objects.filter(title=request.POST['title'])
        if len(title_test) > 0:
            messages.error(request, "Show with this title already exists. Choose another title.")
            return redirect('/shows/new')

        errors = Show.objects.basic_validator(request.POST)

        if len(errors) > 0:
            for value in errors.values():
                messages.error(request, value)
            return redirect('/shows/new')

        new_show = Show.objects.create(title=request.POST['title'], release_date=request.POST['released'], description=request.POST['desc'], network=Network.objects.get(id=request.POST['network']))
        return redirect(f'/shows/ {new_show.id}')

    context = {
        "networks": Network.objects.all()
    }
    return render(request, 'tv_shows/add.html', context)

def verify_title(request):
    valid = True
    title_test = Show.objects.filter(title=request.POST['title'])
    if len(title_test) > 0:
        valid = False

    return render(request,'tv_shows/title-partial.html', {'valid': valid})

def verify_edit_title(request):
    valid = True
    title_test = Show.objects.filter(title=request.POST['title']).exclude(id=request.POST['id'])
    if len(title_test) > 0:
        valid = False

    return render(request,'tv_shows/title-partial.html', {'valid': valid})
