from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("<int:user_pk>/detail/", views.detail, name="detail"),
    path("<int:user_pk>/update/", views.update, name="update"),
    path("logout/", views.logout, name="logout"),
    path("<int:user_pk>/follow/", views.follow, name="follow"),
    path("<int:user_pk>/delete/", views.delete, name="delete"),
]