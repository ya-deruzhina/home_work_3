from . post import PostView
from . comment import CommentView, Comment_postView
from . wallets import WalletsView
from .detail_wallet import DetailWallet

all = (
    "PostView",
    "CommentView",
    "Comment_postView",
    "WalletsView",
    "DetailWallet"
)
