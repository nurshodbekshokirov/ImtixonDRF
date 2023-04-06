from django.contrib.auth.models import User
from django.db import models
class Suv(models.Model):
    brend = models.CharField(max_length=40)
    narx = models.PositiveIntegerField()
    litr = models.CharField(max_length=10)
    batafsil = models.TextField()

    def __str__(self):
        return self.brend
class Mijoz(models.Model):
    ism = models.CharField(max_length=50)
    tel = models.CharField(max_length=20)
    manzil = models.CharField(max_length=50)
    qarz = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism


class Admin(models.Model):
    ism = models.CharField(max_length=50)
    yosh = models.PositiveSmallIntegerField()
    ish_vaqti = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism

class Haydovchi(models.Model):
    ism = models.CharField(max_length=50)
    tel = models.CharField(max_length=30)
    kiritilgan_sana = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.ism

class Buyurtma(models.Model):
    suv = models.ForeignKey(Suv, on_delete=models.CASCADE)
    sana = models.DateField(auto_now_add=True)
    miqdori = models.PositiveSmallIntegerField(null=True)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    umumiy_narxi = models.PositiveIntegerField()
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    haydovchi = models.ForeignKey(Haydovchi, on_delete=models.CASCADE)
# Create your models here.
