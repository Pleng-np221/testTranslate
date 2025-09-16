from django.urls import path
from . import views

urlpatterns = [
    path("translate/<int:blog_id>/", views.translate_blog, name="translate_blog"),
]
