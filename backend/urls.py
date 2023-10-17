from django.urls import path

from backend import views

urlpatterns = [
    # category page
    path('categorypage/', views.categorypage, name="categorypage"),
    path('indexpage/', views.indexpage, name="indexpage"),
    path('categorysave/', views.categorysave, name="categorysave"),
    path('categorydisplay/', views.categorydisplay, name="categorydisplay"),
    path('categoryedit/<int:dataid>/', views.categoryedit, name="categoryedit"),
    path('categoryupdate/<int:dataid>/', views.categoryupdate, name="categoryupdate"),
    path('categorydelete/<int:dataid>/', views.categorydelete, name="categorydelete"),

    # product page
    path('productpage/',views.productpage,name="productpage"),
    path('productsave/',views.productsave,name="productsave"),
    path('productdisplay/',views.productdisplay,name="productdisplay"),
    path('productedit/<int:dataid>/',views.productedit,name="productedit"),
    path('productupdate/<int:dataid>/',views.productupdate,name="productupdate"),
    path('productdelete/<int:dataid>/',views.productdelete,name="productdelete"),

    # admin page
    path('adminpage/',views.adminpage,name="adminpage"),
    path('adminsave/',views.adminsave,name="adminsave"),
    path('adminlogut/',views.adminlogut,name="adminlogut"),

]
