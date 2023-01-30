from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CrawlSerializer
from .models import Crawl
import requests, jsonify
from bs4 import BeautifulSoup

# Create your views here.
def front(request):
    context = { }
    return render(request, "index.html", context)

@api_view(['GET', 'POST'])
def crawl(request):
    if request.method == 'GET':
        crawl = Crawl.objects.all()
        serializer = CrawlSerializer(crawl, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        url = request.data['title']
        soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        serializer = CrawlSerializer(data={
            'title': soup.title.text
        })
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def crawl_detail(request, pk):
    try:
        crawl = Crawl.objects.get(pk=pk)
    except Crawl.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        crawl.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)