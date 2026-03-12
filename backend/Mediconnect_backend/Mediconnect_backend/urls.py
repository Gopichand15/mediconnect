"""
URL configuration for Mediconnect_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hospital/',include('hospital.urls')),
<<<<<<< HEAD
    path('doctors/',include('doctors.urls')), 
    path('accounts/',include('accounts.urls')), 
    path('authentication/',include('authentication.urls')),
    path('patient/',include('patient.urls')),
    path('reviews/',include('reviews.urls'))
    
    
=======

    path('authentication/',include('authentication.urls')),



    path('doctors/',include('doctors.urls')),  
    path('appointment/',include('appointment.urls')),  
    path('patient/', include('patient.urls')),  
>>>>>>> 68b1f3bc52eb52f6bfeaf6c2e7af5fb77b3bf0b8
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

<<<<<<< HEAD
    

=======
>>>>>>> 68b1f3bc52eb52f6bfeaf6c2e7af5fb77b3bf0b8
