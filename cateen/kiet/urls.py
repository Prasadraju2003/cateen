from django.urls import path
from . import views

urlpatterns =[
    path("additem",views.add,name="add"),
    path("mycart",views.cart,name="cart"),
    path("signup",views.signup,name="signup"),
    path("",views.login_view,name="login"),
    
]
   