from . import views
from django.urls import path


urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:slug>/', views.BlogPost.as_view(), name='post_detail'),
]
