from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect

from django.urls import reverse

from .models import Category

def home(request):
    category = Category.objects.all()
    return render(request, 'index.html', context={'category': category})

def about(request):
    return render(request, 'about.html')