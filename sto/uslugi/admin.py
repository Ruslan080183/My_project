from django.contrib import admin
from .models import RemontAvto, TechObsluz, Diagnostika

admin.site.register(RemontAvto)
admin.site.register(TechObsluz)
admin.site.register(Diagnostika)