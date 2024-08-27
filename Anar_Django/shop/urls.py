from django.urls import path
from . import views

urlpatterns = [
    # path('shops/',views.shop,name='shop'),
    path('shops/',views.shopPost.as_view(),name='shop'),
    path('shopping/',views.shopping,name='shopping'),
    # path('shop/<int:pk>',views.singleProduct,name='singleProduct'),
    # path('shop/<int:pk>',views.SinglePostProduct.as_view(),name='singleProduct'),
    path('shop/<int:pk>',views.SingleDetailView.as_view(),name='singleProduct'),
    path('wishlist/',views.wishlist,name='wishlist'),
]