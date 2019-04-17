from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,userProfileForm
from .models import Profile
from django.contrib.auth.models import User




# Create your views here.

def Signup(request):
   
        if request.method == 'POST':
            profile_form = userProfileForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid() and profile_form.is_valid():
                user = form.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Your account has been created! You are now able to log in')
                return redirect('Login')
        else:
            profile_form = userProfileForm()
            form = UserRegisterForm()
        return render(request, 'users/Signup.html', {'form': form, 'profile_form':profile_form})
        

@login_required
def profile(request):
    return render(request, 'users/profile.html')
