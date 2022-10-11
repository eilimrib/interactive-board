from django.urls import path 
from board.views.card_views import cards, card_detail
from board.views.list_views import lists, list_detail

# define the urls
urlpatterns = [
    path("cards/", cards, name="cards"),
    path("cards/<int:pk>/", card_detail, name="card-detail"),
    path("lists/", lists, name="lists"),
    path("lists/<int:pk>/", list_detail, name="list-detail"),
]
