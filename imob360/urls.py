from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("buy_properties/", views.buy, name='buy_properties'),
    path("rent_properties/", views.rent, name='rent_properties'),
    path("sell_property/", views.sell, name='sell_property'),
    path("property_details/", views.pdetails, name='property_details'),
    path("contact_us/", views.contactus, name='contact_us'),
    path("about_us/", views.aboutus, name='about_us'),
    path("lots_and_land/", views.lots_and_land, name='lots_and_land'),
    path("new_developments/", views.new_developments, name='new_developments'),
    path("help/", views.help, name='help'),
    path("login/", views.login, name='login'),
    path("logout/", views.logout, name='logout'),
    path("register/", views.register, name='register'),
    path("home/", views.home, name='home'),  # Added for home path
]
