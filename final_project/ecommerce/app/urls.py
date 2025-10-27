from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cart', views.cart, name="cart"),
    path('categories', views.categories, name="categories"),
    path('contacts', views.contacts, name="contacts"),
    path('faqs', views.faqs, name="faqs"),
    path('log_in', views.log_in, name="log_in"),
    path('shop', views.shop, name="shop"),
    path('sign_up', views.sign_up, name="sign_up"),
    path('whishlist', views.whishlist, name="whishlist"),
]