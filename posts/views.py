from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages 

# Create your views here.
@login_required
def addpost(request):
    print("inside posts app")
    
    return render(request,"posts/addpost.html")
