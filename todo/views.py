from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login


# Create your views here.

def signupuser(request):
    if request.method == 'GET':
        # display sign up form
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})
    else:
        # create new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': 'Username already taken'})

        else:
            # tell user that passwords don't match
            return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': 'Passwords did not match'})

def currenttodos(request):
    return render(request, 'todo/currenttodos.html')
