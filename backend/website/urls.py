from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("contact/", views.contact, name="contact"),
    path("product/<int:product_id>/", views.detail, name="detail")
]
