from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages 
from .models import Profile
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm

# Create your views here.
# def signup(request):
#     print("Inside django form")
#     if request.method == 'POST':
#         print("Django form Submit")
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#     else:
#         form = UserCreationForm()

#     return render(request,"users/signup.html",{'form':form})

def signup(request):
    print("Inside django form")
    if request.method == 'POST':
        print("Django form Submit")
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
    else:
        form = UserRegisterForm()
    return render(request,"users/signup.html",{'form':form})

@login_required
def profile(request):
    print("inside profile")
    if request.method == 'POST':
        user_form=UserUpdateForm(request.POST,instance=request.user)
        try:
            profile_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        except Exception as e:
            profile=Profile(user=request.user)
            profile_form=ProfileUpdateForm(request.POST,request.FILES,instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your Profile has been updated!')


    else:
        user_form=UserUpdateForm(instance=request.user)
        try:
            profile_form=ProfileUpdateForm(instance=request.user.profile)
        except Exception as e:
            profile=Profile(user=request.user)
            profile_form=ProfileUpdateForm(instance=profile)
    context={
        "u_form":user_form,
        "p_form":profile_form
    }
    return render(request,"users/profile.html",context)