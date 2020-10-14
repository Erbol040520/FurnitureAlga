from django.db import models


class FurnitureCard(models.Model):
    title = models.CharField(max_length=250)
    anons = models.TextField()
    img_picture = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return (self.title)
    

class FurnitureCardTwo(models.Model):
    title = models.CharField(max_length=250)
    # anons = models.TextField()
    price = models.CharField(max_length=50,default='')
    img_picture_1 = models.ImageField(upload_to='images/')
    img_picture_2 = models.ImageField(upload_to='images/')
    img_picture_3 = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return (self.title)