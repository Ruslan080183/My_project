# Generated by Django 4.1.4 on 2023-01-22 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uslugi', '0001_create_model_remontavto'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechObsluz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech', models.CharField(max_length=200, verbose_name='ТО')),
                ('vid_tech', models.CharField(choices=[('1', 'Развал-схождение'), ('2', 'Шиномонтаж'), ('3', 'Замена масла'), ('4', 'Замена ремня ГРМ'), ('5', 'Замена фильтров'), ('6', 'Замена фильтров'), ('7', 'Замена сцепления'), ('8', 'Замена тормозной жидкости'), ('9', 'Замена антифриза'), ('10', 'Замена приводных ремней'), ('10', 'Замена ремня генератора')], default='1', max_length=200, verbose_name='Вид ТО')),
                ('repair_description_tech', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Вид ТО',
                'verbose_name_plural': 'Виды ТО',
            },
        ),
    ]
