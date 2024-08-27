# from django.urls import path
# from . import views

# urlpatterns = [
#     # Shop URLs
#     path('shops/', views.ShopListCreateView.as_view(), name='shop-list-create'),
#     path('shops/<int:pk>/', views.ShopRetrieveUpdateDestroyView.as_view(), name='shop-detail'),

#     # ProductVersion URLs
#     path('product-versions/', views.ProductVersionListCreateView.as_view(), name='product-version-list-create'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    # Shop URLs
    path('shops/', views.ShopListCreateView.as_view(), name='shop-list-create'),
    path('shops/<int:pk>/', views.ShopRetrieveUpdateDestroyView.as_view(), name='shop-detail'),

    # ProductVersion URLs
    path('product-versions/', views.ProductVersionListCreateView.as_view(), name='product-version-list-create'),
    # Если нужно добавить URL для отдельного ProductVersion (Retrieve, Update, Delete), добавьте следующий путь
    # path('product-versions/<int:pk>/', views.ProductVersionRetrieveUpdateDestroyView.as_view(), name='product-version-detail'),
]
