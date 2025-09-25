from django.urls import path
from .views import BookListView,BookDetailView
urlpatterns = [
    path('booklist',BookListView.as_view(),name='book_list'),
    path('book/<uuid:pk>/',BookDetailView.as_view(),name='book_detail')
    
]
