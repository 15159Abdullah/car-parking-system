
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('frontend/', include('frontend.urls')),
    path('backend/', include('backend.urls')),
    path('accounts/', include('accountss.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
