from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

from basic.models import Product
from order.models import Shopcart, ShopcartForm, OrderForm, Order, OrderProduct
from user.models import Profile


@login_required
def addtoshopcart(request, pk):
    url = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=pk)
    user = Profile.objects.get(user=request.user)
    data, _ = Shopcart.objects.get_or_create(user=user, product=product)

    if request.method == "POST":
        form = ShopcartForm(request.POST)
        if form.is_valid():
            data.quantity += int(form.cleaned_data.get('quantity'))
            data.save()
            messages.success(request, 'Product succeccfully added to shopcart!')
            return redirect(url)


def shopcart(request):
    current_user = request.user
    user = Profile.objects.get(user=request.user)
    shopcart_ = Shopcart.objects.filter(user=user)
    total = 0
    for rs in shopcart_:
        total += rs.product.price * rs.quantity
    context = {
        'shopcart': shopcart_,
        'total': total,
    }
    return render(request, 'order/shopcart.html', context)


@login_required(login_url='/login')  # check login
def deletefromcart(request, pk):
    Shopcart.objects.filter(id=pk).delete()
    messages.success(request, "Your item deleted from Shop Cart!")
    return redirect('order:shopcart')


def orderproduct(request):
    profile = Profile.objects.get(user=request.user)
    shopcart_ = Shopcart.objects.filter(user=profile)
    total_quantity = 0
    total = 0
    for rs in shopcart_:
        total += rs.product.price * rs.quantity
        total_quantity += rs.quantity
    # return HttpResponse(str(total))

    if request.method == 'POST':  # if there is a post
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.first_name = form.cleaned_data.get('first_name', None)  # get product quantity from form
            data.last_name = form.cleaned_data.get('last_name', None)
            data.last_name = form.cleaned_data.get('email', None)
            data.last_name = form.cleaned_data.get('country', None)
            data.user_id = request.user.id
            data.total = total
            data.total_quantity = total_quantity
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(10).upper()  # random code
            data.code = ordercode
            data.save()

            # Move Shopcart items to Order Product items
            profile = Profile.objects.get(user=request.user)
            shopcart_ = Shopcart.objects.filter(user=profile)
            for rs in shopcart_:
                detail = OrderProduct()
                detail.order_id = data.id  # Order id
                detail.product_id = rs.product_id
                detail.user = profile
                detail.quantity = rs.quantity
                detail.price = rs.product.price
                detail.amount = rs.amount
                detail.save()
                product = Product.objects.get(id=rs.product_id)
                product.amount -= rs.quantity
                product.save()

            Shopcart.objects.filter(user=profile).delete()
            request.session['cart_items'] = 0
            messages.success(request, "Your Order Has Been Completed! Thank you!")
            return render(request, 'order/ordercomplete.html', {'ordercode': ordercode})
        else:
            messages.warning(request, form.errors)
            return redirect('order:orderproduct')

    form = OrderForm
    profile = Profile.objects.get(user=request.user)
    shopcart_ = Shopcart.objects.filter(user_id=profile)
    context = {
        'shopcart': shopcart_,
        'total': total,
        'profile': profile,
        'form': form,
    }

    return render(request, 'order/orderproduct.html', context)
