from django.urls import path
from .views import *

urlpatterns = [    
    path('book-list', bookList, name='book-list'),
    path('book-create', bookCreate, name='book-create'),
    path('book-update/<int:id>', bookUpdate, name='book-update'),
    path('book-delete/<int:id>', bookDelete, name='book-delete'),
    path('book-details/<int:id>', bookDetails, name='book-details'),
    path('book-like/<int:id>/', like_book, name='book-like'),
    path('book-dislike/<int:id>/', dislike_book, name='book-dislike'),
]