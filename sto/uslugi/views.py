
from django.views.generic import ListView
from .models import RemontAvto, TechObsluz, Diagnostika


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