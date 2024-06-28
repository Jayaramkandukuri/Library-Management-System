# library/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('books/', views.book_list, name='book_list'),  
    path('authors/', views.author_list, name='author_list'), 
    path('borrowers/',views.borrower_list, name='borrower_list'),
    # Add more URL patterns as needed for specific views
    path('add-book/', views.add_book, name='add_book'),
    path('add-author/', views.add_author, name='add_author'),
    path('add-borrower/', views.add_borrower, name='add_borrower'),
]
