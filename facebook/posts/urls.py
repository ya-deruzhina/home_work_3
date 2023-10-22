from django.urls import path
from . import views

urlpatterns = [
    path("all",views.get_all_posts),
    path("id/<int:post_id>",views.post_by_id),
    path("counter/<int:count>",views.post_by_counter),
    path("exept_id/<int:post_id>",views.post_exept_id),
    path("exept_counter/<int:count>",views.post_exept_counter),
    path("create",views.create_post),
    path("update/<int:post_id>",views.update_post),
    path("delete/<int:post_id>",views.delete_post)
]