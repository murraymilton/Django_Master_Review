from django.urls import path
from .views import book_list, book_details

urlpatterns = [
    path("book-list/", book_list),
    path("book-details/<int:id>", book_details, name="book-detail"),
]