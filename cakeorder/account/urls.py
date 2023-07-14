from django.urls import path
from .views import*




urlpatterns = [
    path("reg",RegView.as_view(),name="reg"),
    path("home",Home.as_view(),name="h"),
    path("log",LogView.as_view(),name="log"),
    path("ga",Gallery.as_view(),name="g"),
    path("co",Contact.as_view(),name="co"),
    path("abt",Aboutus.as_view(),name="abt"),
    
    path("lgout",Logoutview.as_view(),name='lgout'),
    
    
]
