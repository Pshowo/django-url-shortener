from django.conf import settings
from random import choice
from string import ascii_letters, digits

# Try to get the value from the settings module
SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 8)

AVAIABLE_CHARS = ascii_letters + digits

def random_url_short(model_instance):
    random_url = "".join([choice(AVAIABLE_CHARS) for _ in range(SIZE)])

    model = model_instance.__class__
    if model.objects.filter(url_short=random_url).exists():
        return random_url_short(model_instance)
    return random_url