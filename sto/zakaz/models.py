from django.db import models

class ZakazVidaUslRab(models.Model):
    name = models.CharField("Имя", max_length=150)
    telefon = models.CharField("Телефон", max_length=150)
    data = models.DateField("Дата")
    avto = models.CharField("Марка и модель авто", max_length=200)

    def __str__(self):
        return F"{self.name} {self.telefon} {self.data} {self.avto}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'