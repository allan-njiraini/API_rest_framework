from django.urls import path
from brand.views import product_list

urlpatterns = [
    path('products/', product_list),
]
