# Напишите ваше первое представление

Напишем первое представление. Откройте файл `polls/views.py` и вставьте в него следующий код на Python:

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

Это самое простое представление в Django. Чтобы вызвать представление, нам нужно сопоставить его с URL - и для этого нам нужен URLconf.

Чтобы создать URLconf в директории polls, создайте файл с именем `urls.py`. Теперь ваша структура директории приложения должна выглядеть так:

```plaintext
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py
```

В файле `polls/urls.py` включите следующий код:

```python
from django.urls import path

from. import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

Следующим шагом является указание корневого URLconf на модуль `polls.urls`. В `mysite/urls.py` добавьте импорт для `django.urls.include` и вставьте `~django.urls.include` в список `urlpatterns`, чтобы у вас получилось:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```

Функция `~django.urls.include` позволяет ссылаться на другие URLconf.每当 Django 遇到`~django.urls.include`时，它会切掉到该点为止匹配的 URL 的任何部分，并将剩余的字符串发送到包含的 URLconf 进行进一步处理。

`~django.urls.include`背后的想法是使 URL 的即插即用变得容易。由于投票在自己的 URLconf（`polls/urls.py`）中，它们可以放在“/polls/”下，或“/fun_polls/”下，或“/content/polls/”下，或任何其他路径根目录下，应用程序仍然可以正常工作。

> Когда использовать `~django.urls.include()`
> Вы должны всегда использовать `include()` при включении других URL-шаблонов. `admin.site.urls` - единственное исключение из этого правила.

Теперь вы подключили представление `index` к URLconf. Проверьте, что все работает с помощью следующей команды:

```bash
python manage.py runserver 0.0.0.0:8080
```

Перейдите в браузере по адресу <http://<url>/polls/>, и вы должны увидеть текст "_Hello, world. You're at the polls index._", который вы определили в представлении `index`.

![Django URLconf structure](../assets/20230907-13-51-48-aOKKfCBX.png)

Функция `~django.urls.path` передается четыре аргумента, два обязательных: `route` и `view`, и два необязательных: `kwargs` и `name`. На этом этапе стоит обсудить, для чего эти аргументы.

## Аргумент `~django.urls.path`: `route`

`route` - это строка, содержащая шаблон URL. При обработке запроса Django начинает с первого шаблона в `urlpatterns` и просматривает список сверху вниз, сравнивая запрошенный URL с каждым шаблоном, пока не найдет совпадение.

Шаблоны не ищут GET и POST параметры, или имя домена. Например, в запросе к `https://www.example.com/myapp/` URLconf будет искать `myapp/`. В запросе к `https://www.example.com/myapp/?page=3` URLconf также будет искать `myapp/`.

## Аргумент `~django.urls.path`: `view`

Когда Django находит совпадающий шаблон, он вызывает указанную функцию представления с объектом `~django.http.HttpRequest` в качестве первого аргумента и любые "захваченные" значения из маршрута в качестве именованных аргументов. Мы приведем пример этого чуть позже.

## Аргумент `~django.urls.path`: `kwargs`

Любые именованные аргументы можно передать в виде словаря в целевой вид. Мы не будем использовать эту функцию Django в этом руководстве.

## Аргумент `~django.urls.path`: `name`

Назначение имени URL позволяет ссылаться на него однозначно из других частей Django, особенно из шаблонов. Эта мощная функция позволяет вам вносить глобальные изменения в URL-шаблоны вашего проекта, не трогая при этом более одного файла.
