from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from boardApps import views

urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    path('boardApps/', include('boardApps.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)