from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register(r"country", CountryViewSet, basename="countrys"),
router.register(r"directory", DirectoryViewSet, basename="directorys"),
router.register(r"actor", ActorViewSet, basename="actors"),
router.register(r"genre", GenreViewSet, basename="genres"),

router.register(r"movie_language", MovieLanguagesViewSet, basename="movie_languages"),
router.register(r"moments", MomentsViewSet, basename="momentis"),
router.register(r"rating", RatingViewSet, basename="ratings"),
router.register(r"favorite", FavoriteViewSet, basename="favorites"),
router.register(r"favorite_movie", FavoriteMovieViewSet, basename="favorite_movies"),
router.register(r"history", HistoryViewSet, basename="historys"),


urlpatterns = [
    path("", include(router.urls)),
    # movie
    path("movie/", MovieListAPIView.as_view(), name='movie_list'),
    path("movie/<int:pk>/", MovieDetailAPIView.as_view(), name='movie_detail'),
    path('user/', UserListAPIView.as_view(), name='user-list'),
    path('user/<int:pk>/', UserEditAPIView.as_view(), name='user-detail'),
]
