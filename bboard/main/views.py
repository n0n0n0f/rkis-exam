from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, UserProfile, Order
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    latest_products = Product.objects.all()[:5]
    return render(request, 'main/index.html', {'latest_products': latest_products})


# views.py

from django.urls import reverse


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST, request.FILES)
        if user_form.is_valid():
            user = user_form.save()

            if hasattr(user, 'userprofile'):
                user.userprofile.avatar = request.FILES.get('profile_picture')
                user.userprofile.save()
            else:
                UserProfile.objects.create(user=user, avatar=request.FILES.get('profile_picture'))

            login_url = reverse('main:login')

            return redirect(login_url)
    else:
        user_form = UserRegistrationForm()

    return render(request, 'main/register.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:home')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('main:home')


@login_required
def profile(request):
    return render(request, 'main/profile.html')


def service(request):
    products = Product.objects.all()
    return render(request, 'main/service.html', {'products': products})


def service(request):
    query = request.GET.get('q')

    if query:
        products = Product.objects.filter(title__icontains=query)
    else:
        products = Product.objects.all()

    context = {'query': query, 'products': products}
    return render(request, 'main/service.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'main/product_detail.html', {'product': product})


def order_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    Order.objects.create(user=request.user, product=product)

    return redirect('main:profile')


@login_required
def profile(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'main/profile.html', {'orders': orders})
