from rest_framework import routers, serializers, viewsets
from board.models.card_model import Card

class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'title', 'content', 'list', 'order', 'created_at']