from django.urls import path
from .views.comment import CommentView, OneComment, Create_Comment, Transit_Get_Comment, Delete_Comment
from .views.post import PostView, Delete_Post, PostsView, Transit_Get_Post, Transit_Update_Post

urlpatterns = [
    path("<int:post_id>/",PostView.as_view()),
    
    path("create/",PostsView.as_view()),
    path("",PostsView.as_view()),

    path("<int:post_id>/delete/",Delete_Post.as_view()),

    path("about_comments/<int:post_id>",CommentView.as_view()),
    path("<int:post_id>/comments/",CommentView.as_view()),

    path("comment/<int:comment_id>/",OneComment.as_view()), 
    path("comment/create/",Create_Comment.as_view()), 
    path("comment/<int:comment_id>/delete/",Delete_Comment.as_view()),
    path("<int:post_id>/comment/create/",Create_Comment.as_view()),


    path("create_post/",Transit_Get_Post.as_view()),
    path("<int:post_id>/update/",Transit_Update_Post.as_view()),

    path("<int:post_id>/create_comment/",Transit_Get_Comment.as_view()),
    
]



    # path("all_posts/<int:post_id>",PostView.as_view()),
    # path("delete_post/",PostView.as_view()),
