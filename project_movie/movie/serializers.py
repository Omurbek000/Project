from .models import (
    User,
    Country,
    Directory,
    Actor,
    Genre,
    Movie,
    MovieLanguages,
    Moments,
    Rating,
    Favorite,
    FavoriteMovie,
    History,
)
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["country_name"]


class DirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Directory
        fields = ["director_name"]


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["actor_name"]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["genre_name"]


class MovieLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ["languages", "video"]


class MomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = ["movie_moments"]


class RatingSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format="%d-%m-%Y")
    user = UserSimpleSerializer()
    
    class Meta:
        model = Rating
        fields = ['id', 'user', 'text', 'parent', 'stars', 'created_date']


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = "__all__"


class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = "__all__"


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = "__all__"


class MovieListSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format="%Y")
    genre = GenreSerializer(many=True)
    country = CountrySerializer(many=True)

    class Meta:
        model = Movie
        fields = [
            "id",
            "movie_name",
            "movie_image",
            "year",
            "genre",
            "country",
            "status_movie",
        ]


class MovieDetailtSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format("%d-%m-%Y"))
    genre = GenreSerializer(many=True)
    country = CountrySerializer(many=True)
    director = DirectorySerializer(many=True)
    actor = ActorSerializer(many=True)
    movie_videos = MovieLanguagesSerializer(many=True, read_only=True)
    moments = MomentsSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = [
            "id",
            "movie_name",
            "movie_image",
            "year",
            "genre",
            "country",
            "status_movie",
            "descriptions",
            "movie_trailer",
            "director",
            "actor",
            "movie_videos",
            "moments",
            "ratings",
        ]
