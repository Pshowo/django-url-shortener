from rest_framework import serializers
from .models import Shortener


class UrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shortener
        fields = [
            'id', 
            'time_added', 
            'count',
            'url_long', 
            'url_short', 
            'user_ip', 
            'user_agent']
        