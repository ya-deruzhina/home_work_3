from django.urls import path
# from . import my_views
# from .views import post, comment
# возможно в этой строке надо импортировать не файлы, а классы
# from .views import post, comment, wallet, detail_wallet
from .views import *
from .my_views import *
from .views.post import PostsView, Transit_Get_Post,Transit_Update_Post,Delete_Post
from .views.comment import OneComment,CommentView, Transit_Get_Comment, Create_Comment, Delete_Comment


urlpatterns = [
    # path("all",post.get_all_posts),
    path("id/<int:post_id>",post_by_id),
    path("counter/<int:count>",post_by_counter),
    path("exept_id/<int:post_id>",post_exept_id),
    path("exept_counter/<int:count>",post_exept_counter),
    # path("create",create_post),
    path("update/<int:post_id>",post.update_post),
    path("delete/<int:post_id>",delete_post),
    path("comment",create_comment),
    path("all_comment/<int:post_id>",get_comment),
    path("change_comment",change_comment),
    # path("all_posts/<int:post_id>",post.PostView.as_view()),
    path("about_comments/<int:post_id>",comment.CommentView.as_view()),
    path("change/<int:post_id>",comment.Comment_postView.as_view()),

    path("wallets/",WalletsView.as_view()),
    path("wallets/<int:_id>",DetailWallet.as_view()),
    path("",PostsView.as_view()),
    path("<int:post_id>/",PostView.as_view()),
    path("create_post/",Transit_Get_Post.as_view()),
    path("<int:post_id>/create_comment/",Transit_Get_Comment.as_view()),
    # path("delete_post/",PostView.as_view()),
    path("<int:post_id>/comments/",CommentView.as_view()),
    path("comments/<int:post_id>/",Transit_Get_Post.as_view()),
    path("comment/<int:comment_id>/",OneComment.as_view()), 
    # path("comment/create/",Create_Comment.as_view()), 
    path("<int:post_id>/update/",Transit_Update_Post.as_view()),
    path("<int:post_id>/delete/",Delete_Post.as_view()),
    path("comment/<int:comment_id>/delete/",Delete_Comment.as_view()),
    path("<int:post_id>/comment/create/",Create_Comment.as_view()),
    path("create/",PostsView.as_view()),
]