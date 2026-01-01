from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This points to the file above
    path('productos/', include('productos.urls')),
]
