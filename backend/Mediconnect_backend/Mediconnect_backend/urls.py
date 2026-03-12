from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
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
=======
    path('hospital/', include('hospital.urls')),
    path('authentication/', include('authentication.urls')),
    path('doctors/', include('doctors.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 652df91169b0af49a2284db9722f18fd5a54c09f
