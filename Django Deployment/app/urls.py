from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutusers, name='logout'),
    path('index/', views.index, name='index'),
    path('', views.landingpage, name='landingpage'),
    path('prediction/', views.predict_crop, name='prediction_crop'),

]