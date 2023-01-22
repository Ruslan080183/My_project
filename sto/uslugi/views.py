
from django.views.generic import ListView
from .models import RemontAvto, TechObsluz, Diagnostika


class RemontAvtoListView(ListView):
    model = RemontAvto
    template_name = 'index.html'

class TechObsluzListView(ListView):
    model = TechObsluz
    template_name = 'index2.html'

class DiagnostikaListView(ListView):
    model = Diagnostika
    template_name = 'index3.html'
