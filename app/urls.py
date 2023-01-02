from django.urls import path
from . import views
urlpatterns = [
  
  path('',views.login),
  path('welcome/',views.welcome),
  path('otp/',views.otp),
  path("send_otp",views.send_otp,name="send otp"),
  
  

]
  