# django-url-shortener

## API

- GET - _get all urls list_

    `/v1/api/urls/`

- POST - _post a new url and get shorten url_

    `/v1/api/urls/`

    JSON:

        {
        "url_long": "Put here your long url address"
        }

> python3, django, drf, docker, test

Aplikacja umożliwiająca skracanie linków przez
użytkowników (podobną do bit.ly, link.do) za pomocą REST API.
Zakres funkcjonalności:
- [ ] API przyjmuje adres URL do skrócenia,
- [ ] po podaniu poprawnego adresu wygenerowany zostanie unikalny krótki link,
- długość generowanego krótkiego linku powinna być konfigurowalna (wystarczy na poziomie ustawień projektu),
- [ ] po wejściu w krótki link użytkownik powinien zostać przekierowany do strony docelowej,
- [ ] w przypadku podania przez użytkownika adresu, który został wcześniej podany system nie powinien tworzyć nowego, a jedynie zwrócić istniejący krótki link,
- [ ] *“moduł statystyk” umożliwiający sprawdzenie liczby odwiedzin danego linku,*
- [ ] *możliwość sprawdzenia informacji o osobie, która dodała dany link (IP, user agent)*