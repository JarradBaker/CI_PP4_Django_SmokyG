from . import views
from django.urls import path


urlpatterns = [
    path('bookings/', views.booking_list, name='bookings'),
    path('bookings/create/', views.create_booking, name='create_booking'),
    path('bookings/<int:booking_id>/edit/', views.edit_booking, name='edit_booking'),
    path('bookings/<int:booking_id>/delete/', views.delete_booking, name='delete_booking'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>/comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('<slug:slug>/comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('<slug:slug>/', views.BlogPost.as_view(), name='post_detail'),
    path('', views.blog, name='blog'),
]
