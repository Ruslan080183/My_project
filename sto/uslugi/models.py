from django.db import models

class RemontAvto(models.Model):
    REMO_CHOICES = [
        ("Ремонт подвески", "Ремонт подвески"),
        ("Ремонт двигателя", "Ремонт двигателя"),
        ("Ремонт выхлопной системы", "Ремонт выхлопной системы"),
        ("Ремонт рулевого управления", "Ремонт рулевого управления"),
        ("Ремонт системы охлаждения", "Ремонт системы охлаждения"),
        ("Ремонт тормозной системы", "Ремонт тормозной системы"),
        ("Ремонт электрооборудования", "Ремонт электрооборудования"),
        ("Ремонт МКПП", "Ремонт МКПП"),
        ("Ремонт AКПП", "Ремонт AКПП")
    ]
    remont = models.CharField("Ремонт", max_length=200)
    vid_remonta = models.CharField("Вид ремонта", max_length=200, choices=REMO_CHOICES, default="1")
    repair_description_avto = models.TextField("Описание")

    def __str__(self):
        return self.vid_remonta
    class Meta:
        verbose_name = 'Вид ремонта'
        verbose_name_plural = 'Виды ремонта'
class TechObsluz(models.Model):
    TECHNO_CHOICES = [
        ("Развал-схождение", "Развал-схождение"),
        ("Шиномонтаж", "Шиномонтаж"),
        ("Замена масла", "Замена масла"),
        ("Замена ремня ГРМ", "Замена ремня ГРМ"),
        ("Замена фильтров", "Замена фильтров"),
        ("Замена фильтров", "Замена фильтров"),
        ("Замена сцепления", "Замена сцепления"),
        ("Замена тормозной жидкости", "Замена тормозной жидкости"),
        ("Замена антифриза", "Замена антифриза"),
        ("Замена приводных ремней", "Замена приводных ремней"),
        ("Замена ремня генератора", "Замена ремня генератора"),
    ]
    tech = models.CharField("ТО", max_length=200)
    vid_tech = models.CharField("Вид ТО", max_length=200, choices=TECHNO_CHOICES, default="1")
    repair_description_tech = models.TextField("Описание")

    def __str__(self):
        return self.vid_tech
    class Meta:
        verbose_name = 'Вид ТО'
        verbose_name_plural = 'Виды ТО'

class Diagnostika(models.Model):
    DIAGNO_CHOICES = [
        ("Диагностика подвески", "Диагностика подвески"),
        ("Диагностика двигателя", "Диагностика двигателя"),
        ("Диагностика турбин", "Диагностика турбин"),
        ("Диагностика электрооборудования", "Диагностика электрооборудования"),
        ("Компьютерная диагностика", "Компьютерная диагностика"),

    ]
    diagn = models.CharField("Диагностика", max_length=200)
    vid_diagn = models.CharField("Вид дагностики", max_length=200, choices=DIAGNO_CHOICES, default="1")
    repair_description_diagn = models.TextField("Описание")

    def __str__(self):
        return self.vid_diagn
    class Meta:
        verbose_name = 'Вид диагностики'
        verbose_name_plural = 'Виды диагностики'