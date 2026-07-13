from django.db import models

class Anime(models.Model):
    GENRE_CHOISE=[
    ('action', 'Jangari'),
    ('adventure', 'Sarguzasht'),
    ('comedy', 'Komediya'),
    ('drama', 'Drama'),
    ('fantasy', 'Fantastika'),
    ('romance', 'Romantika'),
    ('horror', "Qo'rqinchli"),
    ]
    title=models.CharField(max_length=100)
    genre=models.CharField(max_length=50,choices=GENRE_CHOISE)
    image=models.ImageField(upload_to='covers/')
    description = models.TextField()

    def __str__(self):
        return self.title