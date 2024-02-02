# yourproject/urls.py
from django.contrib import admin
from django.urls import include, path
from nuvion import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('home/',views.home),
    path('termsandcondition/',views.home),
    path('privacypolicy/',views.home),
    path('workwithus/', include('workwithus.urls')),
]
