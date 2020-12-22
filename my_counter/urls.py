from django.urls import path
from . import views	

urlpatterns = [
    path('',views.index),
    path('/',views.index),
    path('destroy_session', views.destroy),
    path('addtwo', views.addTwo),
    path('addby',views.addby)
]
                    