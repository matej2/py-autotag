from rest_framework import serializers


class HashtagSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)