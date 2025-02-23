# Генерация ошибки 404

Теперь давайте рассмотрим представление деталей вопроса - страницу, на которой отображается текст вопроса для заданного опроса. Вот представление:

```python
from django.http import Http404
from django.shortcuts import render

from.models import Question


#...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})
```

Новая концепция здесь: представление вызывает исключение `~django.http.Http404`, если вопрос с запрошенным ID не существует.

Мы поговорим о том, что можно поместить в шаблон `polls/detail.html` чуть позже, но если вы хотите быстро запустить вышеприведенный пример, файл, содержащий только:

```html+django
{{ question }}
```

будет для вас началом работы на данный момент.

## Короткая запись: `~django.shortcuts.get_object_or_404`

Очень часто используется следующая последовательность действий: использовать `~django.db.models.query.QuerySet.get` и вызывать `~django.http.Http404`, если объект не существует. Django предоставляет короткую запись для этого. Вот представление `detail()`, переписанное:

```python
from django.shortcuts import get_object_or_404, render

from.models import Question


#...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
```

Функция `~django.shortcuts.get_object_or_404` принимает модель Django в качестве первого аргумента и произвольное количество именованных аргументов, которые она передает в функцию `~django.db.models.query.QuerySet.get` менеджера модели. Она вызывает исключение `~django.http.Http404`, если объект не существует.

Почему мы используем вспомогательную функцию `~django.shortcuts.get_object_or_404`, а не автоматически ловим исключения `~django.core.exceptions.ObjectDoesNotExist` на более высоком уровне или заставляем API модели вызывать `~django.http.Http404` вместо `~django.core.exceptions.ObjectDoesNotExist`?

Поскольку это привяжет модельный слой к представительному слою. Одной из главных целей дизайна Django является поддержание слабой связи. Некоторое контролируемое связывание вводится в модуле `django.shortcuts`.

Также существует функция `~django.shortcuts.get_list_or_404`, которая работает так же, как `~django.shortcuts.get_object_or_404`, за исключением того, что она использует `~django.db.models.query.QuerySet.filter` вместо `~django.db.models.query.QuerySet.get`. Она вызывает исключение `~django.http.Http404`, если список пуст.
