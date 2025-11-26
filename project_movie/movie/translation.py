from .models import Country, Directory, Actor, Genre, Movie, MovieLanguages
from modeltranslation.translator import register, TranslationOptions

@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = (
        'country_name',
    )

@register(Directory)
class DirectoryTranslationOptions(TranslationOptions):
    fields = (
        'director_name',
        'bio',
    )

@register(Actor)
class ActorTranslationOptions(TranslationOptions):
    fields = (
        'actor_name',
        'bio',
    )
@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = (
        'genre_name',
    )

@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = (
        'movie_name',
        'descriptions',
    )

@register(MovieLanguages)
class MovieLanguagesTranslationOptions(TranslationOptions):
    fields = (
        'languages',
    )