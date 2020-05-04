import json

from django.http import JsonResponse
from django.shortcuts import render
import requests
import re


def random_hashtags(request):
    URL = 'https://www.instagram.com/explore/tags/handmade/?__a=1'

    # sending get request and saving the response as response object
    r = requests.get(url=URL)
    data = (r.json())

    posts = data["graphql"]["hashtag"]["edge_hashtag_to_top_posts"]["edges"]

    all_hashtags = []

    for post in posts:
        content = post["node"]
        caption = content["edge_media_to_caption"]["edges"]
    return JsonResponse((
        type(caption)
    ), safe=False)
        #hashtags = re.search(r'(#\w*)\s', caption)
        #for i in range(5):
       #     all_hashtags.append(hashtags[i])

    #return JsonResponse(all_hashtags, safe=False)

