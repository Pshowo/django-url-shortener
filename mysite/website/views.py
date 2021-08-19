from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView
from api.models import Shortener


class Urls(ListView):
    model = Shortener
    paginate_by = 25
    allow_empty = True
    queryset = Shortener.objects.all()
    context_object_name = 'urls'
    template_name = 'website/urls.html'


def url_details(request, url_id):
    if Shortener.objects.filter(id=url_id).exists():
        url = Shortener.objects.filter(id=url_id).first()
        context = {"url": url}
        return render(request, 'website/detail.html', context)
    else:
        raise Http404("Url does not exist")
