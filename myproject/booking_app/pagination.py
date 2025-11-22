from rest_framework.pagination import PageNumberPagination


class HotelSetPagination(PageNumberPagination):
    page_size = 5


class RoomSetPagination(PageNumberPagination):
    page_size = 8
