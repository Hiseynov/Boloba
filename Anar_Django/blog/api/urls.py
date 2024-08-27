from django.urls import path

from . import views

urlpatterns = [
    # path('blog/',views.Blog,name='blog'),
    path('blogs/',views.BlogApiCreateList.as_view(),name='blog'),
    path('blogs/<int:pk>/',views.BlogApiUpdateList.as_view(),name='blog_detailsApi')
]