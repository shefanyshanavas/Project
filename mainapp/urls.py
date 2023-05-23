
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # user routing
    path('', include('clientapp.urls')),

    # admin routing
    path('admin/', include('adminapp.urls')),

    # service - center url routing
    path('service-center/', include('serivceapp.urls')),

    # path('database/', admin.site.urls),

    # api routing
    path('api/', include('clientapp.urls')),
    path('service-api/', include('serivceapp.urls')),
]
