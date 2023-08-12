from . import views
from django.urls import path
from smoky_g.views import blog


urlpatterns = [
    path('', smoky_g.views.blog, name='blog'),
    path('<slug:slug>/', views.BlogPost.as_view(), name='post_detail'),
]
