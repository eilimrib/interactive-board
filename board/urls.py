from django.urls import path 
from board.views.card_views import cards, card_detail

# define the urls
urlpatterns = [
    path('cards/', cards),
    path('cards/<int:pk>/', card_detail),
]