from django.db import models
from django.contrib.auth.models import User


class Advertisement(models.Model):
    TANKI = 'TANKI'
    HILY = 'HILY'
    DD = 'DD'
    TORGOVCI = 'TORGOVCI'
    GILDMASTERI = 'GILDMASTERI'
    KVESTGIVERI = 'KVESTGIVERI'
    KUZNECI = 'KUZNECI'
    KOZHEVNIKI = 'KOZHEVNIKI'
    ZELEVARI = 'ZELEVARI'
    MASTERA_ZAKLINANIY = 'MASTERA_ZAKLINANIY'     
    CATEGORY = [
        (TANKI, 'Танки'),
        (HILY, 'Хилы'),
        (DD, 'ДД'),
        (TORGOVCI, 'Торговцы'),
        (GILDMASTERI, 'Гилдмастеры'),
        (KVESTGIVERI, 'Квестгиверы'),
        (KUZNECI, 'Кузнецы'),
        (KOZHEVNIKI, 'Кожевники'),
        (ZELEVARI, 'Зельевары'),
        (MASTERA_ZAKLINANIY, 'Мастера заклинаний'),
        ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='img', null=True, blank=True)
    video = models.FileField(upload_to='video', null=True, blank=True)
    files = models.FileField(upload_to='files', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(choices=CATEGORY, max_length=25)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)