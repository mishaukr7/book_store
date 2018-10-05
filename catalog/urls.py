from django.urls import path
from .views import BookListView, BookCreateView, BookUpdateView , RequestListView

app_name = 'catalog'

urlpatterns = [
    path('books', BookListView.as_view(), name='book_list'),
    path('books/add_book', BookCreateView.as_view(), name='add_book'),
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='edit_book'),
    path('requests', RequestListView.as_view(), name='request_list')

]