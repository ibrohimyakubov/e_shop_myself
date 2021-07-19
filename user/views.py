from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from order.models import Order, OrderProduct
from user.forms import UserUpdateForm, ProfileUpdateForm, SignUpForm
from user.models import Profile


@login_required
def my_profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'user/my_profile.html', {'profile': profile})


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # completed sign up
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Your account has been created!')

            return redirect('basic:index')
        else:
            messages.warning(request, form.errors)
            return redirect('user:register')

    form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'user/register.html', context)


def login_(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('basic:index')
        else:
            messages.warning(request, "Login Error, Try again or Sign Up!")
            return redirect('user:login')
    return render(request, 'user/login.html')


@login_required
def logout_func(request):
    logout(request)
    return redirect('basic:index')


@login_required
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated')
            return HttpResponseRedirect('/user')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, 'user/profile_update.html', context)


@login_required
def user_orders(request):
    orders = Order.objects.filter(user_id=request.user.id)
    return render(request, 'user/user_order.html', {'orders': orders})


@login_required
def user_orders_delete(request, pk):
    Order.objects.filter(id=pk).delete()
    messages.success(request, "Your item deleted from Order List!")
    return redirect('user:user-orders')


@login_required
def user_order_detail(request, pk):
    orders = Order.objects.get(user_id=request.user.id, id=pk)
    order_item = OrderProduct.objects.filter(order_id=pk)
    return render(request, 'user/user_order_detail.html', {'order': orders, 'orderitems': order_item})
