import json
from random import shuffle

from django.http import JsonResponse
from django.shortcuts import render
import requests
import re

from TagSuggestions.models import HashtagSearch

tag_search = []
tag_search.append(HashtagSearch("handmade", 50))
tag_search.append(HashtagSearch("homemade", 30))
tag_search.append(HashtagSearch("slovenia", 5))

hashtag_list = []

def random_hashtags(request):

    for search in tag_search:
        URL = f'https://www.instagram.com/web/search/topsearch/?context=blended&query=%23{search.word}&rank_token=0.08962517317904317&include_reel=true'

        r = requests.get(url=URL)
        data = (r.json())

        hashtags = data["hashtags"]

        for i in range(50):
            if i >= search.first:
                break
            text = hashtags[i]["hashtag"]["name"]
            hashtag_list.append(text)

    shuffle(hashtag_list)

    return JsonResponse((
        hashtag_list[:30]
    ), safe=False)
