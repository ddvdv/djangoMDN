from django.urls import path
from catalog import views

urlpatterns = [
        path('', views.index, name='index'),
        path('books/', views.BookListView.as_view(), name="books"),
        path('book/<int:pk>', views.BookDetailView.as_view(), name="book-detail"),
        path('author/', views.AuthorListView.as_view(), name="authors"),
        path('author/<int:pk>', views.AuthorDetailView.as_view(), name="author-detail"),
        path('mybooks/', views.LoanedBookByUserListView.as_view(), name='my-borrowed'),
        path('borrowed/', views.LoanedBookAllListView.as_view(), name='borrowed'),
        path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]
