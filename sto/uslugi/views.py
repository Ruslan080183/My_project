
from django.views.generic import ListView
from .models import RemontAvto, TechObsluz, Diagnostika
from .forms import RemontAvtoForm, TechObsluzForm, DiagnostikaForm
from django.shortcuts import render


def home_view(request):
    context = {}
    context['form'] = RemontAvtoForm()
    return render(request, "uslugi/ind1.html", context)

def home_view1(request):
    context = {}
    context['form'] = TechObsluzForm()
    return render(request, "uslugi/ind21.html", context)

def home_view2(request):
    context = {}
    context['form'] = DiagnostikaForm()
    return render(request, "uslugi/ind31.html", context)

class RemontAvtoListView(ListView):
    model = RemontAvto
    template_name = 'uslugi/index.html'





class TechObsluzListView(ListView):
    model = TechObsluz
    template_name = 'uslugi/index2.html'

class DiagnostikaListView(ListView):
    model = Diagnostika
    template_name = 'uslugi/index3.html'
class DiagnostikaListView1(ListView):
    model = Diagnostika
    template_name = 'uslugi/base.html'

class DiagnostikaListView2(ListView):
    model = Diagnostika
    template_name = 'uslugi/contakt.html'