from django.contrib import admin
from django.urls import path
from .import views
from .views import (
    PostListView,
    PostCreateView,
    PostDetailView,
    PostUpdateview,
    PostDeleteView,
    inpectionList
)
  

urlpatterns = [
    # path('', views.home,name="blog-home"),
    # React rest path here
    path('reactsaveuser/',views.reactsaveuser,name="Signup"),
    path('rehome/',views.rehome,name="Home"),
    path('reacthome/',views.reacthome,name="React-Home"),
    path('blog/test/',views.test,name="React-test"),
    path('test1/',views.test1,name="blog-test1"),
    path('chartview/',views.chartview,name="ChartFlow"),


    # django path here

    path('',PostListView.as_view(),name='blog-home'),
    path('post/new/',PostCreateView.as_view(),name='Post-Create'),
    path('post<int:pk>/',PostDetailView.as_view(),name='Post-Details'),
    path('about/',views.about,name="blog-about"),
    path('post<int:pk>/update/',PostUpdateview.as_view(),name='Post-Update'),
    path('post<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),

    # React demo session
    path('reactlogin/',views.reactlogin,name="Jav-SignIn"),
    path('register/',views.register,name="JAV-SignUP"),


    path('inspectionlist/',views.inpectionList,name="inspectionList"),
]
