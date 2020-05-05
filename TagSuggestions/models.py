from django.db import models

# Create your models here.


class HashtagSearch():
    def __init__(self, word, first):
        self.word = word
        # "First" parameter makes sure only most popular hashtags are included, assuming list is properly ordered
        self.first = first
