from datetime import datetime
from django.contrib import messages
from django.shortcuts import render
from decimal import Decimal

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Bus, Book
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from decimal import Decimal


def home(request):
    if request.user.is_authenticated:
        return render(request, 'a1/home.html')
    else:
        return render(request, 'a1/signin.html')


@login_required(login_url='signin')
def findbus(request):
    context = {}
    
    # Fetch distinct sources and destinations for dropdown menus
    context['sources'] = Bus.objects.values_list('source', flat=True).distinct()
    context['destinations'] = Bus.objects.values_list('dest', flat=True).distinct()
    
    if request.method == 'POST':
        source_r = request.POST.get('source')
        dest_r = request.POST.get('destination')
        date_r = request.POST.get('date')

        # Validate form inputs
        if not source_r or not dest_r or not date_r:
            context['error'] = "All fields are required."
            context['data'] = request.POST
            return render(request, 'a1/findbus.html', context)

        if source_r == dest_r:
            context['error'] = "Source and destination cannot be the same."
            context['data'] = request.POST
            return render(request, 'a1/findbus.html', context)
        
        try:
            # Parse date input
            date_r = datetime.strptime(date_r, "%Y-%m-%d").date()
        except ValueError:
            context['error'] = "Invalid date format. Please enter a valid date."
            context['data'] = request.POST
            return render(request, 'a1/findbus.html', context)
        
        # Filter buses based on source, destination, and date
        bus_list = Bus.objects.filter(
            source=source_r, 
            dest=dest_r, 
            date__year=date_r.year, 
            date__month=date_r.month, 
            date__day=date_r.day
        )
        
        # Render the results page if buses are found
        if bus_list.exists():
            return render(request, 'a1/list.html', {'bus_list': bus_list, 'date': date_r, 'source': source_r, 'destination': dest_r})
        else:
            context['error'] = "No available Bus Schedule for the entered Route and Date."
            context['data'] = request.POST
            return render(request, 'a1/findbus.html', context)
    else:
        # Render the form page with dropdown menus
        return render(request, 'a1/findbus.html', context)


@login_required(login_url='signin')
def bookings(request):
    context = {}
    if request.method == 'POST':
        bus_name_r = request.POST.get('bus_name')
        seats_r = int(request.POST.get('no_seats'))
        try:
            bus = Bus.objects.get(bus_name=bus_name_r)
            if bus.rem >= seats_r:
                cost = seats_r * bus.price
                username_r = request.user.username
                email_r = request.user.email
                userid_r = request.user.id
                rem_r = bus.rem - seats_r
                Bus.objects.filter(id=bus.id).update(rem=rem_r)
                book = Book.objects.create(
                    name=username_r,
                    email=email_r,
                    userid=userid_r,
                    bus_name=bus.bus_name,
                    source=bus.source,
                    busid=bus.id,
                    dest=bus.dest,
                    price=bus.price,
                    nos=seats_r,
                    date=bus.date,
                    time=bus.time,
                    status='BOOKED'
                )
                print('------------book id-----------', book.id)
                return render(request, 'a1/bookings.html', locals())
            else:
                context["error"] = "Sorry, not enough seats available"
                return render(request, 'a1/findbus.html', context)
        except Bus.DoesNotExist:
            context["error"] = "Bus not found"
            return render(request, 'a1/findbus.html', context)

    else:
        return render(request, 'a1/findbus.html')


@login_required(login_url='signin')
def cancellings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('bus_id')
        #seats_r = int(request.POST.get('no_seats'))

        try:
            book = Book.objects.get(id=id_r)
            bus = Bus.objects.get(id=book.busid)
            rem_r = bus.rem + book.nos
            Bus.objects.filter(id=book.busid).update(rem=rem_r)
            #nos_r = book.nos - seats_r
            Book.objects.filter(id=id_r).update(status='CANCELLED')
            Book.objects.filter(id=id_r).update(nos=0)
            messages.success(request, "Booked Bus has been cancelled successfully.")
            return redirect(seebookings)
        except Book.DoesNotExist:
            context["error"] = "Sorry You have not booked that bus"
            return render(request, 'a1/error.html', context)
    else:
        return render(request, 'a1/findbus.html')


@login_required(login_url='signin')
def seebookings(request,new={}):
    context = {}
    id_r = request.user.id
    book_list = Book.objects.filter(userid=id_r)
    if book_list:
        return render(request, 'a1/booklist.html', locals())
    else:
        context["error"] = "Sorry no buses booked"
        return render(request, 'a1/findbus.html', context)


def signup(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        email_r = request.POST.get('email')
        password_r = request.POST.get('password')
        user = User.objects.create_user(name_r, email_r, password_r, )
        if user:
            login(request, user)
            return render(request, 'a1/thank.html')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'a1/signup.html', context)
    else:
        return render(request, 'a1/signup.html', context)


def signin(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        password_r = request.POST.get('password')
        user = authenticate(request, username=name_r, password=password_r)
        if user:
            login(request, user)
            # username = request.session['username']
            context["user"] = name_r
            context["id"] = request.user.id
            return render(request, 'a1/success.html', context)
            # return HttpResponseRedirect('success')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'a1/signin.html', context)
    else:
        context["error"] = "You are not logged in"
        return render(request, 'a1/signin.html', context)


def signout(request):
    context = {}
    logout(request)
    context['error'] = "You have been logged out"
    return render(request, 'a1/signin.html', context)


def success(request):
    context = {}
    context['user'] = request.user
    return render(request, 'a1/success.html', context)
