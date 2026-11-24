from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, get_product_by_category

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename = 'products')

urlpatterns = [

    path('categories/<slug:slug>/', get_product_by_category, name='product_list_by_category' ),

    # path('products', ProductViewSet.as_view(), name='product_list'),
    # path('categories/<slug:slug>/', get_product_by_category, name='product_list_by_category'),
]

urlpatterns += router.urls

print("generated ")