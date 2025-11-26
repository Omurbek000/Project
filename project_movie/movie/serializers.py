from .models import (User, Country, Directory, Actor, Genre, Movie, MovieLanguages, Moments, Rating, Favorite, FavoriteMovie, History)
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

        
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"
 

class DirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Directory
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
     class Meta:
        model = Genre
        fields = "__all__"
 
 
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
 
class MovieLanguagesSerializer(serializers.ModelSerializer):
     class Meta:
        model = MovieLanguages
        fields = "__all__"
      

class MomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = "__all_ "

class RatingSerializer(serializers.ModelSerializer):
     class Meta:
         model = Rating
         fields = "__all__"     
 
 

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
 
       