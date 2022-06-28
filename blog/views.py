from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def root_page(request):
    return render(request, 'blog/index.html')
