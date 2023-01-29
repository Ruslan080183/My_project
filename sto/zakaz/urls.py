from django.urls import path, include
from .views import ZakazVidaUslRabListView, zak2_page

urlpatterns = [

    path('zak/', ZakazVidaUslRabListView.as_view()),
    path("zak2/", zak2_page, name='zak2'),

]