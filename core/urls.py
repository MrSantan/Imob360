"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('buy_properties/', include("imob360.urls")),
    path('rent_properties/', include("imob360.urls")),
    path('sell_property/', include("imob360.urls")),
    path('property_details/', include("imob360.urls")),
    path('contact_us/', include("imob360.urls")),
    path('about_us/', include("imob360.urls")),
    path('lots_and_land/', include("imob360.urls")),
    path('new_developments/', include("imob360.urls")),
    path('help/', include("imob360.urls")),
    path('login/', include("imob360.urls")),
    path('logout/', include("imob360.urls")),
    path('register/', include("imob360.urls")),
    path('', include("imob360.urls")),
]
