from django.db import models
from userapp.models import Account


class Bolim(models.Model):
    nom = models.CharField(max_length=50)
    rasm = models.FileField(upload_to="bolimlar", blank=True)
    def __str__(self):
        return self.nom

class Ichki(models.Model):
    nom = models.CharField(max_length=100)
    rasm = models.FileField(upload_to="ichki bolimlar")
    bolim = models.ForeignKey(Bolim, on_delete=models.SET_NULL, null=True, related_name="bolim_ichkilari")
    def __str__(self):
        return self.nom

class Mahsulot(models.Model):
    nom = models.CharField(max_length=200)
    narx = models.IntegerField()
    ishlab_ch = models.CharField(max_length=300)
    kafolat = models.CharField(max_length=50)
    yetkazish = models.CharField(max_length=200)
    olchov = models.CharField(max_length=200, blank=True)
    min_buyurtma = models.CharField(max_length=200, blank=True)
    mavjud = models.BooleanField(default=True)
    batafsil = models.CharField(max_length=500)
    ichki = models.ForeignKey(Ichki, on_delete=models.SET_NULL, null=True, related_name="ichki_mahsulotlari")
    def __str__(self):
        return self.nom

class Media(models.Model):
    rasm = models.FileField(upload_to="mahsulotlar")
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.SET_NULL, null=True, related_name="mahsulot_rasmi")

class Comment(models.Model):
    mijoz = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    izoh = models.CharField(max_length=300)
    baho = models.PositiveSmallIntegerField(default=4)
    sana = models.DateTimeField(auto_now_add=True)

