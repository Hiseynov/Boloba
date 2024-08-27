from django.urls import path

from . import views

urlpatterns = [
    path("time/",views.time,name='time'),
    # path('contact/',views.contact,name='contact'),
    # path('contact/',views.ContactView.as_view(),name='contact'),
    path('contact/',views.ContactListVies.as_view(),name='contact'),
    path('checkout/',views.checkout,name='checkout'),
    path('create/',views.CreatePostView.as_view(),name='create'),
    path('update/<int:pk>',views.UpdatePostView.as_view(),name='update'),
    path('delete/<int:pk>',views.DeletePostView.as_view(),name='delete'),
    path('set_language/', views.change_language, name='set_language'),
]