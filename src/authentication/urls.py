from django.urls import path
from .views import loginUser,logoutUser,dashboard


app_name = 'authentication'

urlpatterns = [
    path('', loginUser, name="login"),
    path('logout', logoutUser, name="logOut"),
    path('dashboard', dashboard, name="dashboard"),
]
