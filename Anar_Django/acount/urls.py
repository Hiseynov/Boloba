# from django.urls import path

# from . import views

# urlpatterns = [
#     path('login/',views.Login,name='login'),
#     path('register/',views.Register,name='register')
# ]
from django.urls import path
from .views import (CustomLoginView,
                    RegisterView,
                    CustomPasswordResetView,
                    CustomPasswordResetConfirmView,
                    activate,logout_view
                    )
                   
# from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('confirmation/<str:uidb64>/<str:token>/', activate, name='confirmation'),
    path('logout/', logout_view, name='logout'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_confirm/<str:uidb64>/<str:token>/',
        CustomPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
]