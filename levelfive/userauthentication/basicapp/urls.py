from django.urls import path
from basicapp import views

app_name="basicapp"
urlpatterns=[
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.userlogin,name='userlogin'),
    path('logout/',views.userlogout,name='userlogout'),
    path('special/',views.special,name='special'),

]
