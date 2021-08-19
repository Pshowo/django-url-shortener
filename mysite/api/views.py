from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Shortener
from .forms import ShortenerForm
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UrlSerializer
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from string import ascii_letters, digits
import requests

SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 8)
AVAIABLE_CHARS = ascii_letters + digits

def random_url_short():
    random_url = "".join([choice(AVAIABLE_CHARS) for _ in range(SIZE)])
    if Shortener.objects.filter(url_short=random_url).exists():
        return random_url_short()
    return random_url

# ==== Views ====

def index(request):
    context = {}
    context['form'] = ShortenerForm()

    if request.method == 'GET':
        return render(request, "api/index.html", context)
    elif request.method == 'POST':
        form_ = ShortenerForm(request.POST)
        if form_.is_valid():

            shortened_object = form_.save()

            context['new_url'] = request.build_absolute_uri("/") + shortened_object.url_short
            context['long_url'] = shortened_object.url_long
            return render(request, "api/index.html", context)
        context['error'] = form_.errors

    return render(request, "api/index.html", context)

def redirect_url(request, short_url):
    print(short_url)
    short_url = request.get_host() + "/" + short_url
    if Shortener.objects.filter(url_short=short_url).exists():
        short = Shortener.objects.get(url_short=short_url)
        short.count += 1
        short.save()

        return HttpResponseRedirect(short.url_long)
    else:
        return Http404("This link doesn't exist.")

from random import choice
from string import ascii_letters, digits


class UrlsViewSet(viewsets.ModelViewSet):

    serializer_class = UrlSerializer

    def get_queryset(self):
        queryset = Shortener.objects.all()
        return queryset
    
    def create(self, request, *args, **kwargs):
        
        validate = URLValidator()
        try:
            validate(request.data['url_long'])
        except ValidationError as e:
            if request.data['url_long'].find("http") == -1:
                return Response({'msg': "Did you forget about 'http'?"})
            return Response({'msg': "Wrong url address"})
        res = requests.get(request.data['url_long'])

        if 200 <= res.status_code < 400:
            if Shortener.objects.filter(url_long=request.data['url_long']).exists():
                qs = Shortener.objects.get(url_long=request.data['url_long'])
                serializer = UrlSerializer(qs, many=False)
                return Response(serializer.data)
            else:
                new_url = Shortener.objects.create(
                    url_short = request.get_host() + "/" + random_url_short(),
                    url_long=request.data['url_long'],
                    user_ip = request.META.get('REMOTE_ADDR'),
                    user_agent = request.META.get('HTTP_USER_AGENT'))
                
                serializer = UrlSerializer(new_url, many=False)
                serializer.data['url_short'] = "bla"
                return Response(serializer.data)
        else:
            return Response({'msg': "This URL address not response"})
