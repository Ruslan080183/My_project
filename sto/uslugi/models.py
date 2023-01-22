from django.db import models

class RemontAvto(models.Model):
    REMO_CHOICES = [
        ("1", "Ремонт подвески"),
        ("2", "Ремонт двигателя"),
        ("3", "Ремонт выхлопной системы"),
        ("4", "Ремонт рулевого управления"),
        ("5", "Ремонт системы охлаждения"),
        ("6", "Ремонт тормозной системы"),
        ("7", "Ремонт электрооборудования"),
        ("8", "Ремонт МКПП"),
        ("9", "Ремонт AКПП")
    ]
    remont = models.CharField("Ремонт", max_length=200)
    vid_remonta = models.CharField("Вид ремонта", max_length=200, choices=REMO_CHOICES, default="1")
    repair_description_avto = models.TextField("Описание")

    def __str__(self):
        return self.vid_remonta
    class Meta:
        verbose_name = 'Вид ремонта'
        verbose_name_plural = 'Виды ремонта'
