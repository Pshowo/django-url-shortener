from django.shortcuts import render
from django.views.generic import ListView
from api.models import Shortener


class Urls(ListView):
    queryset = Shortener.objects.all().order_by('time_added')
    paginate_by = 25
    context_object_name = 'urls'
    template_name = 'website/urls.html'