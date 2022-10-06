from rest_framework import routers, serializers, viewsets
from board.models.list_model import List

class ListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = List
        fields = ['id', 'title']