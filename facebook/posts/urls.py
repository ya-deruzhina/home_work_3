from django.urls import path
from . import views

urlpatterns = [
    path("list", views.get_post_first),
    path("all", views.get_posts),
    path("<int:post_id>", views.get_post),
    path("create", views.create_post)
]