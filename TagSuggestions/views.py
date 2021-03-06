import json
from random import shuffle

from django.http import JsonResponse
from django.shortcuts import render
import requests
import re

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from TagSuggestions.models import HashtagSearch

hashtag_list = []
num_of_hashtags = 10


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def random_hashtags(request):
    shuffled_list = []

    tag_search = []
    request_tags = []

    try:
        request_tags = request.data
    except IndexError:
        print('No body header found!')

    for hashtag in request_tags:
        print(hashtag)
        tag_search.append(HashtagSearch(hashtag['name'], hashtag['freq']))

    for search in tag_search:
        URL = f'https://www.instagram.com/web/search/topsearch/?context=blended&query=%23{search.word}&rank_token=0.08962517317904317&include_reel=true'

        r = requests.get(url=URL)
        data = (r.json())

        hashtags = data["hashtags"]

        for i in range(search.first):
            text = hashtags[i]["hashtag"]["name"]
            print(f"adding {text}")
            hashtag_list.append(text)

    shuffle(hashtag_list)
    shuffled_list = list(map(lambda x: '#' + x, hashtag_list[:num_of_hashtags]))

    return JsonResponse({
        'list': shuffled_list,
        'string': ' '.join(shuffled_list),
    }, safe=False)
