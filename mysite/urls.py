from django.conf.urls import include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainApp.urls')),
    path('news/', include('news.urls'))
]
