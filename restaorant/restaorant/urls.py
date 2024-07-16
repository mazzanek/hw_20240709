from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('rest/', include('add_view.urls')),
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
]