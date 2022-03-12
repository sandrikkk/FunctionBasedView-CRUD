from statistics import fmean
from django.http import HttpResponseRedirect
from django.shortcuts import render

import studentscrud
from .forms import StudentRegistration
from .models import User
# Create your views here.
def index(request):
    if request.method == 'POST':
        forms = StudentRegistration(request.POST)
        if forms.is_valid():
            nm = forms.cleaned_data['name']
            em = forms.cleaned_data['email']
            pw = forms.cleaned_data['password']
            reg = User(name = em, email = em, password = pw)
            reg.save()
            fm = StudentRegistration()
    else:
        forms = StudentRegistration()
    students = User.objects.all()
    return render(request, 'studentscrud/add.html', {
        "forms":forms,
        "students": students
    })

def update_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk = id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        else:
            pi = User.objects.get(pk = id)
            fm = StudentRegistration(instance=pi)
    else:
        fm = StudentRegistration(instance=pi)
    return render(request, "studentscrud/update.html", {
        'form':fm
    })

def delete_data(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk = id)
        pi.delete()
        return HttpResponseRedirect('/')
