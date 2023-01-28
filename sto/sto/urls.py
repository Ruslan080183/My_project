"""sto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from uslugi.views import home_view, home_view1, home_view2, RemontAvtoListView, TechObsluzListView, DiagnostikaListView, DiagnostikaListView1, DiagnostikaListView2
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', RemontAvtoListView.as_view()),
    path('index2/', TechObsluzListView.as_view()),
    path('index3/', DiagnostikaListView.as_view()),
    path('', DiagnostikaListView1.as_view()),
    path('contakt/', DiagnostikaListView2.as_view()),
    path('ind1/', home_view),
    path('ind21/', home_view1),
    path('ind31/', home_view2),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
