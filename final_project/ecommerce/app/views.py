from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def cart(request):
    return render(request, "cart.html")

def categories(request):
    return render(request, "categories.html")

def contacts(request):
    return render(request, "contacts.html")

def faqs(request):
    return render(request, "faqs.html")

def log_in(request):
    return render(request, "log_in.html")

def shop(request):
    return render(request, "shop.html")

def sign_up(request):
    return render(request, "sign_up.html")

def whishlist(request):
    return render(request, "whishlist.html")

