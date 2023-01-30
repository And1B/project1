from rest_framework import serializers
from .models import Crawl

class CrawlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crawl
        fields = '__all__'