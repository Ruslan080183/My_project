
from .views import  home_view, home_view1, home_view2, RemontAvtoListView, TechObsluzListView, DiagnostikaListView, DiagnostikaListView1, DiagnostikaListView2
from django.urls import path

urlpatterns = [

    path('index/', RemontAvtoListView.as_view()),
    path('index2/', TechObsluzListView.as_view()),
    path('index3/', DiagnostikaListView.as_view()),
    path('', DiagnostikaListView1.as_view()),
    path('contakt/', DiagnostikaListView2.as_view()),
    path('ind1/', home_view),
    path('ind21/', home_view1),
    path('ind31/', home_view2),

]