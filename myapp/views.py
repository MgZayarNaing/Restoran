from django.shortcuts import render
from .models import *
# Create your views here.

def category_list(request):
    category = Category.objects.all().order_by('-id')
    return render(request, 'index.html', {'category': category})