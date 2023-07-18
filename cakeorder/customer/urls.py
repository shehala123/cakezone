from django.urls import path
from .views import*

urlpatterns = [
    path('chome',CustHomeView.as_view(),name="ch"),
    path('search',Search.as_view(),name='search'),
    path('prodet/<int:pid>',Productdetailview.as_view(),name="pdet"),
    path('acart/<int:id>',AddCart.as_view(),name="acart"),
    path('cartv',Cartlistview.as_view(),name="vcart"),
    path('dcart/<int:id>',deletecart,name="decart"),
    path('check/<int:cid>',Checkout.as_view(),name="checkout"),
    path('orders',OrderView.as_view(),name="order"),
     path('cancelorder/<int:id>',cancel_order,name="orderc"),
    
   
]
