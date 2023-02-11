from django.urls import path
from .views import product_list, product_detail


urlpatterns = [


    path('list/', product_list, name='product_list'),
    path('list/<int:category_slug>/', product_list, name='product_list_by_category'),
    path('detail/<int:id>/<int:slug>/', product_detail, name='product_detail'),
]