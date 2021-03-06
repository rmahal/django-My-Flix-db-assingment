# Generated by Django 2.0.5 on 2018-09-11 22:52

from django.db import migrations

def seed(apps, schema_editor):
    User = apps.get_model('myflixdb', 'User')
    Flix = apps.get_model('myflixdb', 'Flix')
    Like = apps.get_model('myflixdb', 'Like')
    Raj = User(username="userRaj", password="userRaj1")
    Luke = User(username="userLuke", password="userLuke1")
    Raj.save()
    Luke.save()
    sharp_objects = Flix(name="sharp objects", backdrop_path="aslkgjeigegegejowj", poster_path="a;oiegjegohgddd", movie_id=4355, overview="s;lgegeg gjeogjwg")
    sharp_objects.save()
    the_office = Flix(name="The Office", backdrop_path="asdasdada", poster_path="a;adadadadad", movie_id=1234, overview="a;adddd ddddaa")
    the_office.save()
    luke_like = Like(user=Luke, flix=sharp_objects)
    luke_like.save()
    raj_like = Like(user=Raj, flix=the_office)
    raj_like.save()


def fallow(apps, schema_editor):
    User = apps.get_model('myflixdb', 'User')
    Flix = apps.get_model('myflixdb', 'Flix')
    Like = apps.get_model('myflixdb', 'Like')
    #User.objects.all().delete()
    #Flix.objects.all().delete()
    #Like.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('myflixdb', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed, fallow)
    ]
