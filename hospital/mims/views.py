from django.shortcuts import render,redirect
from .models import Department,Doctor,Booking
from .forms import BookingForm
from django.contrib import messages

def home(request):
    return render(request,'home.html')
def doctor(request):
     docs = {
        'doc': Doctor.objects.all()
    }
     return render(request,'doctor.html', docs)

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirm.html')
    form = BookingForm()
    dict_form = {
        'form' : form
    }
    return render(request,'booking.html',dict_form)

def department(request):
    dict_dept = {
        'dept': Department.objects.all()
    }
    return render(request,'department.html',dict_dept)

def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def confirming(request):
    return render(request,'confirm.html')
