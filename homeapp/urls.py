from django.urls import path

from homeapp import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('contactus/', views.contactus, name="contactus"),
    path('pro/<catname>/', views.pro, name="pro"),
    path('singleproduct/<int:proid>', views.singleproduct, name="singleproduct"),
    path('register/', views.register, name="register"),
    path('loginpg/', views.loginpg, name="loginpg"),
    path('registersave/', views.registersave, name="registersave"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('logout/', views.logout, name="logout"),
    path('cartsave/', views.cartsave, name="cartsave"),
    path('cartdisplay/', views.cartdisplay, name="cartdisplay"),
    path('cartdel/<int:dataid>/', views.cartdel, name="cartdel"),
    path('checkout/', views.checkout, name="checkout"),
    path('checksave/', views.checksave, name="checksave"),
]
