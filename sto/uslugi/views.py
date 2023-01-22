
from django.views.generic import ListView
from .models import RemontAvto, TechObsluz


class RemontAvtoListView(ListView):
    model = RemontAvto
    template_name = 'index.html'

class TechObsluzListView(ListView):
    model = TechObsluz
    template_name = 'index2.html'
