from django.shortcuts import render
from .models import Post,InspectionList
from .models import User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework import serializers
from rest_framework import viewsets
import pandas as pd
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
# Create your views here.
# posts=[
#     {
#         "author":"Jishnu",
#         "title":"Blog Post1",
#         "content":"First Page Content",
#         "date_posted":"August 13, 2020"
#     },
#     {
#         "author":"Vivek",
#         "title":"Blog Post2",
#         "content":"Second Page Content",
#         "date_posted":"August 9, 2020"
#     }
# ]
# <------------------------------React session demo--------------------------------------------->
# login 
@csrf_exempt
def reactlogin(request):
    # retStatus={"status":"1","message":"Success"}
    try:
        print("Call From React1")
        x=json.loads(request.body)
        print(x)
        data=x["data"]
        username=data["username"]
        password=data["password"]
        print(username)
        print(password)
        # user= User.objects.filter(username=username)
        user=authenticate(username=username,password=password)
        print(user )
        if(user):
            retStatus={"status":"1","message":"Authentication Success"}
        else:
            retStatus={"status":"0","message":"Authentication Fail"}

    except Exception as e:
        print(e)
        retStatus={"status":"0","message":"Fail"}
    return JsonResponse(retStatus)

# Regiteration
@csrf_exempt
def register(request):
    try:
        print("Call From React1")
        x=json.loads(request.body)
        print(x)
        data=x["data"]
        print(data,"reeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        username=data['username']
        mail=data['mail']
        pwd=data['pwd']
        user = User.objects.create_user(username=username, email=mail, password=pwd)
        # user = User.objects.create_superuser(username=data['username'], email=data['mail'], password=data['pwd'])
        print(user)
        if(user):
            retStatus={"status":"1","message":"Your are Submited Successfully..!!"}
        else:
            retStatus={"status":"0","message":"Fail"}
    except Exception as e:
        print(e)
        retStatus={"status":"0","message":"Fail"}
    return JsonResponse(retStatus)

# <----------------------------------------------------Django Session----------------------------------------------------------------------------------------->

def home(request):
    context={
        "posts":Post.objects.all(),
        "title":"Blogers"
    }
    # return HttpResponse("<h1>WeLcOmE Home</h1>")
    return render(request,"blog/home.html",context)

def about(request):
    context={
        "title":"Developer",
        "Content":"Python"
    }
    # return HttpResponse("<h1>WeLComE About</h1>")
    return render(request,"blog/about.html",context) 


class PostListView(ListView):
    model=Post
    template_name = 'blog/home.html'
    context_object_name='posts'
    # ordering = ['date_posted'] #Ascending order
    ordering = ['-date_posted'] #Descending order

class PostDetailView(DetailView):
    model = Post
    context_object_name='post1'


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog-home')

class PostUpdateview(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
        
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
# <------------------------------React session--------------------------------------------->
# react rest test0
@csrf_exempt
def test(request):
    # retStatus={"status":"1","message":"Success"}
    try:
        print("Call From React1")
        x=json.loads(request.body)
        print(x)
        data=x["data"]
        username=data["username"]
        password=data["password"]
        print(username)
        print(password)
        # user= User.objects.filter(username=username)
        user=authenticate(username=username,password=password)
        print(user )
        if(user):
            retStatus={"status":"1","message":"Authentication Success"}
        else:
            retStatus={"status":"0","message":"Authentication Fail"}

    except Exception as e:
        print(e)
        retStatus={"status":"0","message":"Fail"}
    return JsonResponse(retStatus)

# react rest test1
@csrf_exempt
def test1(request):
    # retStatus={"status":"1","message":"Success"}
    try:
        print("Call From React1")
        x=json.loads(request.body)
        print(x)
        data=x["data"]
        username=data["username"]
        password=data["pwd"]
        print(username)
        print(password)
        # user= User.objects.filter(username=username)
        user=authenticate(username=username,password=password)
        print(user )
        if(user):
            retStatus={"status":"1","message":"Authentication Success"}
        else:
            retStatus={"status":"0","message":"Fail"}

    except Exception as e:
        print(e)
        retStatus={"status":"0","message":"Fail"}
    return JsonResponse(retStatus)
# def test1(request):
#     return HttpResponse("<h1>WeLComE..Rest Apl Call is Here...!!</h1>")

# react views 
@csrf_exempt
def reacthome(request):
    posts=[]
    try:
        print("Call From React1")
        posts = Post.objects.all().values()
        print(posts)
        posts_list = list(posts)
        print(posts_list)
    except Exception as e:
        print(e)
    return JsonResponse(posts_list, safe=False) 

@csrf_exempt
def rehome(request):
    posts=[]
    try:
        print("Call From Reacthook Inserted..!!")
        posts = Post.objects.all().values()
        posts_list = list(posts)
        print(posts_list)
    except Exception as e:
        print(e)
    return JsonResponse(posts_list,safe=False)

#  react using saveuser registeration 
@csrf_exempt
def reactsaveuser(request):
    try:
        print("Call From React1")
        x=json.loads(request.body)
        print(x)
        data=x["data"]
        print(data)
        # user = User.objects.create_user(username=data['username'], email=data['mail'], password=data['pwd'])
        user = User.objects.create_superuser(username=data['username'], email=data['mail'], password=data['pwd'])
        print(user)
        if(user):
            retStatus={"status":"1","message":"Your are Submited Successfully..!!"}
        else:
            retStatus={"status":"0","message":"Fail"}
    except Exception as e:
        print(e)
        retStatus={"status":"0","message":"Fail"}
    return JsonResponse(retStatus)

@csrf_exempt
def chartview(request):
    journal_df=None
    report_df=None
    try:
        # journal_df=pd.read_excel('E:/web developing/sampledata.xlsx','Journal',skiprows=[0])
        journal_df=pd.read_excel('E:/web developing/sampledata.xlsx','Journal')
        # retStatus={"status":"1","message":"Success"}
        print(journal_df)
        report_df=journal_df.groupby(['BDate']).last().reset_index()
        report_df=report_df[["BDate","Return(%)"]]
        print(report_df)
    except Exception as e:
        print(e)
        # retStatus={"status":"0","message":"Fail"}

    return JsonResponse(report_df.to_json(orient='split'), safe=False)



# <------------------------------HTC PROJECT--------------------------------------------->

@csrf_exempt
def inpectionList(request):
    posts=[]
    try:
        print("Call From React1")
        posts = InspectionList.objects.all().values()
        print(posts,"INSPECTION LIST")
        posts_list = list(posts)
        print(posts_list)
    except Exception as e:
        print(e)
    return JsonResponse(posts_list, safe=False) 
