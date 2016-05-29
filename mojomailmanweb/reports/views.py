from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return HttpResponse("Hello, world. You're at the reports index.")
# Create your views here.
