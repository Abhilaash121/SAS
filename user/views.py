from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm,UserUpdateForm, ProfileUpdateForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') #we remove all other data and are bothered about username
            messages.success(request, f'Account has been created for {username}. Continue to Log-in')
            return redirect('user-login')
    else:
        form = CreateUserForm()
    context = {
        'formtemp' : form

    }
    return render(request,'user/register.html',context)

@login_required()
def profile(request):
    return render(request, 'user/profile.html')

@login_required()
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your profile has been updated.')
            return redirect('user-profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context ={
        'user_form' : user_form,
        'profile_form' : profile_form
    }
    return render(request, 'user/profile_update.html', context)