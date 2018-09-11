from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username

class Flix(models.Model):
    movie_id = models.IntegerField()
    name = models.CharField(max_length=100)
    poster_path = models.URLField()
    backdrop_path = models.URLField()
    overview = models.TextField()

    def __str__(self):
        return self.name

class Like(models.Model):
    flix = models.ForeignKey(Flix, on_delete=models.CASCADE, related_name='flix')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return f'{self.user.username} likes the movie {self.flix.name}'