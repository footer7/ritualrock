from django.urls import path
from . import views
urlpatterns = [
        path('', views.index),
        path('about/',views.about),
        path('contacts/',views.contacts),
        path('news/',views.news),
        path('prod/',views.prod),
        path('photogallery/',views.photogallery),

]
