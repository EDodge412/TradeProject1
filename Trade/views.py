from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import ListingForm
from .models import listing
from .models import message
from .forms import messageForm
from .forms import checkForm


def home(request):
    return render(request, 'Trade/home.html')


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'Trade/login.html', {'form': form})


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'Trade/register.html', {'form': form})


@login_required(login_url='login')
def my_listings(request):
    listings = listing.objects.filter(user=request.user)
    context = {'listings': listings}
    return render(request, 'Trade/mylistings.html', context)


@login_required(login_url='login')
def view_listings(request):
    listings = listing.objects.all()
    context = {'listings': listings}
    return render(request, 'Trade/listpage.html', context)


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def create_list(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('view_listings')
    else:
        form = ListingForm

    return render(request, 'Trade/create.html', {'form': form})


@login_required(login_url='login')
def search_listing(request):
    search_term = request.GET.get('search-term') or ''
    listings = listing.objects.filter(user=request.user, title__icontains=search_term,
                                      description__icontains=search_term)
    context = {'listings': listings}
    return render(request, 'Trade/listpage.html', context)


@login_required(login_url='login')
def delete_listing(request, listing_id):
    list_item = listing.objects.get(id=listing_id)
    if request.method == 'POST':
        list_item.delete()

    return redirect('my_listings')


@login_required(login_url='login')
def update_listing(request, listing_id):
    listing_item = listing.objects.get(id=listing_id, user=request.user)
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES, instance=listing_item)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('my_listings')
    else:
        form = ListingForm(instance=listing_item)

    return render(request, 'Trade/updatelist.html', {'form': form})


@login_required(login_url='login')
def comment(request):
    if request.method == 'POST':
        form = messageForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('view_listings')
    else:
        form = messageForm

    return render(request, 'Trade/messagelister.html', {'form': form})


@login_required(login_url='login')
def view_comments(request):
    messages = message.objects.filter(user=request.user.id)
    context = {'messages': messages}
    return render(request, 'Trade/comment.html', context)


@login_required(login_url='login')
def buy(request):
    if request == 'POST':
        form = checkForm(request.POST)
        if form.is_valid():
            form.instance = request.user
            form.save()
            return redirect(view_listings)
    else:
        form = checkForm
    return render(request, 'Trade/payment.html', {'form': form})
