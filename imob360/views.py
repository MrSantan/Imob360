from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'properties/home.html')

def buy(request):
    return render(request, 'properties/buy_properties.html')
def rent(request):
    return render(request, 'properties/rent_properties.html')
def sell(request):
    return render(request, 'properties/sell_property.html')
def pdetails(request):
    return render(request, 'properties/property_details.html')
def contactus(request):
    return render(request, 'properties/contact_us.html')
def aboutus(request):
    return render(request, 'properties/about_us.html')
def lots_and_land(request):
    return render(request, 'properties/lots_and_land.html')
def new_developments(request):
    return render(request, 'properties/new_developments.html')
def help(request):
    return render(request, 'properties/help.html')
def login(request):
    return render(request, 'registration/login.html')
def logout(request):
    return render(request, 'registration/logout.html')
def register(request):
    return render(request, 'registration/register.html')
def property_list(request):
    return render(request, 'properties/property_list.html')
def search_results(request):
    return render(request, 'properties/search_results.html')