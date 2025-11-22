from django.urls import include, path
from rest_framework import routers
from .views import (UserProfileListAPIView, UserProfileDetailAPIView,
                    CityListAPIView, CityDetailAPIView,
                    HotelListAPIView, HotelDetailAPIView,
                    RoomListAPIView, RoomDetailAPIView,
                    ReviewCreateAPIView, BookingViewSet,
                    ReviewEditAPIView, HotelViewSet, RegisterView, LogoutView, LoginView)


router = routers.SimpleRouter()
router.register(r'booking', BookingViewSet)
router.register(r'hotel_create', HotelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cities/', CityListAPIView.as_view(), name='city_list'),
    path('cities/<int:pk>/', CityDetailAPIView.as_view(), name='city_detail'),
    path('hotels/', HotelListAPIView.as_view(), name='hotel_list'),
    path('hotels/<int:pk>/', HotelDetailAPIView.as_view(), name='hotel_detail'),
    path('rooms/', RoomListAPIView.as_view(), name='room_list'),
    path('rooms/<int:pk>/', RoomDetailAPIView.as_view(), name='room_detail'),
    path('users/', UserProfileListAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
    path('reviews/', ReviewCreateAPIView.as_view(), name='review_create'),
    path('reviews/<int:pk>/', ReviewEditAPIView.as_view(), name='review_edit'),
]




