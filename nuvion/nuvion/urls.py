# yourproject/urls.py
from django.contrib import admin
from django.urls import include, path
from nuvion import views
handler404 = views.custom_404_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('home/',views.home),
    path('termsandcondition/',views.terms),
    path('privacypolicy/',views.privacy),
    path('workwithus/', include('workwithus.urls')),
]
