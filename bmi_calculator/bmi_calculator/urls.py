from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bmiapp.urls')),  # This includes the URL routing for bmiapp at the root
]
