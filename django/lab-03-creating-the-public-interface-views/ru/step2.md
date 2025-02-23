# Создание дополнительных представлений

Теперь добавим несколько дополнительных представлений в `polls/views.py`. Эти представления немного отличаются, потому что они принимают аргумент:

```python
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

Свяжем эти новые представления с модулем `polls.urls`, добавив следующие вызовы `~django.urls.path`:

Откройте файл `polls/urls.py` и добавьте следующие строки:

```python
from django.urls import path

from. import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

Теперь запустите сервер снова:

```bash
cd ~/project/mysite
python manage.py runserver 0.0.0.0:8080
```

Переключитесь на вкладку **Web 8080** и перейдите по адресу `/polls/34/`. Сервер запустит метод `detail()` и отобразит любой ID, который вы укажете в URL. Попробуйте также `/polls/34/results/` и `/polls/34/vote/` - они отобразят заглушку результатов и страницу голосования.

![Диаграмма маршрутизации URL в Django](../assets/20230908-09-30-06-2n54ROPe.png)

Когда кто-то запрашивает страницу на вашем сайте - скажем, `/polls/34/`, Django загрузит Python-модуль `mysite.urls`, потому что он указан в настройке `ROOT_URLCONF`. Он находит переменную с именем `urlpatterns` и последовательно обходит шаблоны. После нахождения совпадения по `'polls/'` он удаляет совпадающий текст (`"polls/"`) и отправляет оставшийся текст - `"34/"` - в URL-конфигурацию `'polls.urls'` для дальнейшей обработки. Там оно совпадает с `'<int:question_id>/'`, что приводит к вызову представления `detail()` следующим образом:

```python
detail(request=<HttpRequest object>, question_id=34)
```

Часть `question_id=34` берется из `<int:question_id>`. Использование угловых скобок "захватывает" часть URL и передает ее в качестве именованного аргумента в функцию представления. Часть `question_id` в строке определяет имя, которое будет использоваться для идентификации совпавшего шаблона, а часть `int` - это конвертер, который определяет, какие шаблоны должны совпадать с этой частью пути URL. Двоеточие (`:`) отделяет конвертер и имя шаблона.
