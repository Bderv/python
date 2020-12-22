from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	
    path('register',views.register),   
    path('success', views.success),
    path('login', views.login),
    path('logout', views.logout),
    path('quotes', views.addQuote),
    path('createQuote', views.createQuote),
    path('like/<int:contentId>', views.likeContent),
    path('delete/<int:contentId>', views.delete),
    path('users/<int:uploaderId>', views.showUser),
    path('unlike/<int:contentId>', views.unlikeContent),

]