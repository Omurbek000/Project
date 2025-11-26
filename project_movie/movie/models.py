from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

STATUS_CHOICES = (
    ("active", "Active"),
    ("inactive", "Inactive"),
)


class User(AbstractUser):
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(15), MaxValueValidator(100)],
        null=True,
        blank=True,
    )
    phone_number = PhoneNumberField(region="KG", null=True, blank=True)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, default="active")
    date_register = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Country(models.Model):
    country_name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.country_name


class Directory(models.Model):
    director_name = models.CharField(max_length=64)
    bio = models.TextField()
    age = models.DateField()
    director_image = models.ImageField(upload_to="dorector_images/")

    def __str__(self) -> str:
        return self.director_name


class Actor(models.Model):
    actor_name = models.CharField(max_length=64)
    bio = models.TextField()
    age = models.DateField()
    actor_image = models.ImageField(upload_to="actor_images/")

    def __str__(self) -> str:
        return self.actor_name


class Genre(models.Model):
    genre_name = models.CharField(max_length=64, unique=True)

    def __str__(self) -> str:
        return self.genre_name


class Movie(models.Model):
    movie_name = models.CharField(max_length=64)
    year = models.DateField()
    country = models.ManyToManyField(Country)
    director = models.ManyToManyField(Directory)
    actor = models.ManyToManyField(Actor)
    genre = models.ManyToManyField(Genre)
    TYPE_CHOICES = (
        ("144p", "144p"),
        ("360p", "360p"),
        ("480p", "480p"),
        ("720p", "720p"),
        ("1080p", "1080p"),
    )
    types = models.CharField(choices=TYPE_CHOICES, max_length=10)
    movie_time = models.PositiveSmallIntegerField()
    descriptions = models.CharField(max_length=1000)
    movie_trailer = models.FileField(upload_to="movie_trailer/")
    movie_image = models.ImageField(upload_to="movie_images/")
    status_movie = models.CharField(
        max_length=100, choices=STATUS_CHOICES, default="active"
    )

    def __str__(self) -> str:
        return f"{self.movie_name} - {self.year}"


class MovieLanguages(models.Model):
    languages = models.CharField(max_length=32)
    video = models.FileField(upload_to="movie_video/")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_videos')

    def __str__(self) -> str:
        return f"{self.languages}, {self.movie}"


class Moments(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='moments')
    movie_moments = models.ImageField(upload_to="movei_moments")

    def __str__(self) -> str:
        return f"{self.movie}"


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    stars = models.PositiveSmallIntegerField(
        choices=[(i, str(i)) for i in range(1, 11)]
    )
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user} - {self.movie}"


class Favorite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user}"


class FavoriteMovie(models.Model):
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class History(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    viewed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user}"
