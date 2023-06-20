from django.urls import path
from . import views

urlpatterns = [
    path("movies", views.MovieList.as_view()),
    path("movies/<int:pk>", views.MovieDetail.as_view()),
    path("movies/<int:pk>/reviews", views.ReviewList.as_view()),
    path("actors", views.ActorList.as_view()),
    path("actors/<int:pk>", views.ActorDetail.as_view()),
]
