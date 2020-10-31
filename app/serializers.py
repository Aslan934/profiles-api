from rest_framework import serializers


class HelloViewSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
