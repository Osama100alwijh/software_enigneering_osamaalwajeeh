from django.urls import path
from . import views
urlpatterns = [
    path('app4',views.home,name='app4'),
]
