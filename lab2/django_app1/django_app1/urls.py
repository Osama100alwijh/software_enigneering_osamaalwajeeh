from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # أضف هذا السطر

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include('app1.urls')),  # استخدم include بدلاً من الرجوع المباشر
    path('app2/', include('app2.urls')),
    path('app3/', include('app3.urls')),
    path('test/', lambda r: HttpResponse("Test successful!")),
]