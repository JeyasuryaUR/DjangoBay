from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createListing", views.create_listing, name="create_listing"),
    path("listings/<int:pid>", views.listing_view, name="listing"),
    path("listings/<int:pid>/close", views.close_auction, name="close_auction"),
    path("listings/<int:pid>/addWatchlist", views.add_watchlist, name="add_watchlist"),
    path("listings/<int:pid>/newBid", views.new_bid, name="new_bid"),
    path("listings/<int:pid>/comment", views.post_comment, name="comment"),
    path("listings/closed", views.closed, name="closed"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("category/<str:cid>", views.category, name="category")
]
