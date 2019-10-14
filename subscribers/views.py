from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import SubscriberForm

# Create your views here.

def subscribers_new(request, template='subscribers/subscriber_new.html'):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            '''unpack the form values'''
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            '''create a user record'''
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            '''
            create a sunscriber record
            process the payments
            Auto login the user
            '''
            return HttpResponseRedirect('/success/')
        else:
            form = SubscriberForm()
            return render(request, template, {'form':form})
