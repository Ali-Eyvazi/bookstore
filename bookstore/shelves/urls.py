from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from . import views



APP_NAME = 'shelves'
urlpatterns = [
    path('books/', views.BooksView.as_view()),
    path('book/<int:book_id>/',views.BookDetailView.as_view()),

   
]