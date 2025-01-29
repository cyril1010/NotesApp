from django.shortcuts import render,redirect
from .models import NotepadDB

def home(request):
    data = NotepadDB.objects.all()
    return render(request,'HomePage.html', {'data': data})

def add_page(request):
    return render(request,'AddPage.html')

def save_note(request):
    if request.method == "POST":
        ti = request.POST.get('title')
        co = request.POST.get('content')
        noteObj = NotepadDB(title=ti,note=co)
        noteObj.save()
        return redirect(home)


def edit_page(request, note_id):
    data = NotepadDB.objects.get(id=note_id)
    return render(request, 'EditPage.html', {'data': data})


def update_note(request, note_id):
    if request.method == "POST":
        ti = request.POST.get('title')
        co = request.POST.get('content')
        NotepadDB.objects.filter(id=note_id).update(title=ti,note=co)
        return redirect(home)

def delete_note(request, note_id):
    x = NotepadDB.objects.filter(id=note_id)
    x.delete()
    return redirect(home)

