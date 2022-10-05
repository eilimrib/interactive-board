from django.db import models
from board.models.list_model import List 


class Card(models.Model):
    title = models.CharField(max_length=50)
    value = models.IntegerField(default=0)
    content = models.CharField(max_length=500)
    # list = models.ForeignKey(List, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

