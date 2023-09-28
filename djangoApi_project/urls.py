from django.contrib import admin
from django.urls import path
#from django.conf.urls import url
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.BookApiView.as_view())
    
]
