from django.urls import path

from . import views

urlpatterns = [
    # path('blog/',views.Blog,name='blog'),
    path('blogs/',views.BlogPost.as_view(),name='blog'),
    path('blog/<int:pk>/',views.BlogDetailView.as_view(),name='blog_details')
]