from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.views import LoginView
from villageapp.models import Userquery

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

from django.contrib.auth.decorators import login_required
# Create your views here.


def register(req):
    if req.method == 'POST':
        form = UserRegisterForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                req, f'Account is successfully created for {username} ! Now You are able to login')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(req, 'users/register.html', {'form': form})


@login_required
def Profile(req):

    if req.method == 'POST':

        u_form = UserUpdateForm(req.POST, instance=req.user)
        p_form = ProfileUpdateForm(
            req.POST, req.FILES, instance=req.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                req, f'Account information successfully updated !')
            return redirect('village-home')

    else:
        u_form = UserUpdateForm(instance=req.user)
        p_form = ProfileUpdateForm(instance=req.user.profile)
        data = Userquery.objects.all()

    return render(req, 'users/profile.html', {'u_form': u_form, 'p_form': p_form, 'data': data})


class UserLogin(LoginView):
    template_name: str = "login.html"
