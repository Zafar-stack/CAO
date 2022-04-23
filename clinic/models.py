from django.db import models
from sorl.thumbnail import ImageField, get_thumbnail


class Direction(models.Model):
    name = models.CharField("Направление", max_length=200)

    def __str__(self):
        return self.name


class Clinic(models.Model):
    title = models.CharField("Название клиники", max_length=200)
    title2 = models.CharField("ENG название", max_length=200)
    text = models.TextField("Описание")
    image = models.ImageField("Загрузить фото", upload_to='clinic/')
    directions = models.ManyToManyField(Direction, verbose_name="направления")

    def __str__(self):
        return self.title

    def get_image_url(self):
        return get_thumbnail(self.image, '100x100').url
