from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Shortener
from .forms import ShortenerForm

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
    if Shortener.objects.filter(url_short=short_url).exists():
        short = Shortener.objects.get(url_short=short_url)
        short.count += 1
        short.save()

        return HttpResponseRedirect(short.url_long)
    else:
        return Http404("This link doesn't exist.")