from django.shortcuts import render
from .models import ZakazVidaUslRab
from django.views.generic import ListView

class ZakazVidaUslRabListView(ListView):
    model = ZakazVidaUslRab
    template_name = 'zakaz/zak.html'


def zak2_page(request):
    user = request.POST['user']
    tel = request.POST['tel']
    time = request.POST['time']
    cars = request.POST['cars']
    element = ZakazVidaUslRab(name=user, telefon=tel, data=time, avto=cars)
    element.save()
    return render(request, "zakaz/zak2.html", {'user': user, 'tel': tel, 'time': time, 'cars': cars})


