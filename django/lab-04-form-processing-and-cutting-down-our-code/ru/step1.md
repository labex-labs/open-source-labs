# Напишите минимальную форму

Обновим шаблон деталей опроса (`polls/detail.html`) из предыдущего туториала, чтобы он содержал HTML-элемент `<form>`:

```html+django
<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
<fieldset>
    <legend><h1>{{ question.question_text }}</h1></legend>
    {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}
    {% for choice in question.choice_set.all %}
        <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
        <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
    {% endfor %}
</fieldset>
<input type="submit" value="Vote">
</form>
```

Краткий обзор:

- Вышеприведенный шаблон отображает радиокнопку для каждого варианта ответа на вопрос. `value` каждой радиокнопки — это ID соответствующего варианта ответа на вопрос. `name` каждой радиокнопки — `"choice"`. Это означает, что когда кто-то выбирает одну из радиокнопок и отправляет форму, она отправит POST-данные `choice=#`, где \# — это ID выбранного варианта. Это основная концепция HTML-форм.
- Мы установили `action` формы на `{% url 'polls:vote' question.id %}`, и установили `method="post"`. Использование `method="post"` (в отличие от `method="get"`) очень важно, потому что отправка этой формы изменит данные на стороне сервера. Когда вы создаете форму, которая изменяет данные на стороне сервера, используйте `method="post"`. Этот совет не специфичен для Django; это хорошее правило веб-разработки в целом.
- `forloop.counter` показывает, сколько раз тег `for` прошел по циклу
- Поскольку мы создаем POST-форму (которая может иметь эффект изменения данных), нам нужно беспокоиться о межсайтовых подделках запросов. К счастью, вам не нужно слишком сильно беспокоиться, потому что Django имеет полезную систему защиты от этого. Короче говоря, все POST-формы, предназначенные для внутренних URL-адресов, должны использовать шаблонный тег `{% csrf_token %}<csrf_token>`.

Теперь создадим представление Django, которое обрабатывает отправленные данные и делает с ними что-то. Помните, в разделе **Создание представлений для общедоступного интерфейса** мы создали URL-конфигурацию для приложения опросов, которая включает в себя эту строку:

```python
path("<int:question_id>/vote/", views.vote, name="vote"),
```

Мы также создали заглушку реализации функции `vote()`. Создадим настоящую версию. Добавьте следующее в `polls/views.py`:

```python
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from.models import Choice, Question


#...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
```

В этом коде есть несколько вещей, о которых мы еще не говорили в этом туториале:

- `request.POST <django.http.HttpRequest.POST>` — это объект, похожий на словарь, который позволяет вам получать отправленные данные по имени ключа. В этом случае `request.POST['choice']` возвращает ID выбранного варианта в виде строки. `request.POST <django.http.HttpRequest.POST>` значения всегда являются строками.

  Обратите внимание, что Django также предоставляет `request.GET
<django.http.HttpRequest.GET>` для доступа к GET-данным аналогичным образом — но мы явно используем `request.POST
<django.http.HttpRequest.POST>` в нашем коде, чтобы убедиться, что данные изменяются только через вызов POST.

- `request.POST['choice']` вызовет `KeyError`, если `choice` не был предоставлен в POST-данных. Код выше проверяет наличие `KeyError` и переотображает форму вопроса с сообщением об ошибке, если `choice` не указан.

- После увеличения количества голосов код возвращает `~django.http.HttpResponseRedirect`, а не обычный `~django.http.HttpResponse`. `~django.http.HttpResponseRedirect` принимает один аргумент: URL-адрес, на который будет перенаправлен пользователь (см. следующий пункт, как мы строим URL-адрес в этом случае).

  Как указывает комментарий на Python выше, вы должны всегда возвращать `~django.http.HttpResponseRedirect` после успешной обработки POST-данных. Этот совет не специфичен для Django; это хорошее правило веб-разработки в целом.

- В этом примере мы используем функцию `~django.urls.reverse` в конструкторе `~django.http.HttpResponseRedirect`. Эта функция помогает избежать жесткой кодировки URL-адреса в функции представления. Ей передается имя представления, на которое мы хотим передать управление, и переменная часть URL-шаблона, которая указывает на это представление. В этом случае, используя URL-конфигурацию, которую мы установили в разделе **Создание представлений для общедоступного интерфейса**, вызов `~django.urls.reverse` вернет строку, похожую на:

      "/polls/3/results/"

  где `3` — это значение `question.id`. Затем этот перенаправленный URL-адрес вызовет представление `'results'`, чтобы отобразить конечную страницу.

Как упоминалось в разделе **Создание представлений для общедоступного интерфейса**, `request` — это объект `~django.http.HttpRequest`. Для получения дополнительной информации о объектах `~django.http.HttpRequest` см. документацию по запросам и ответам </ref/request-response>.

После того, как кто-то голосует за вопрос, представление `vote()` перенаправляет на страницу результатов для этого вопроса. Напишем это представление:

```python
from django.shortcuts import get_object_or_404, render


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})
```

Это почти точно то же самое, что и представление `detail()` из раздела **Создание представлений для общедоступного интерфейса**. Единственная разница — это имя шаблона. Мы исправим эту избыточность позже.

Теперь создайте шаблон `polls/results.html`:

```html+django
<h1>{{ question.question_text }}</h1>

<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
{% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote again?</a>
```

Теперь перейдите по адресу `/polls/1/` в вашем браузере и голосуйте за вопрос. Вы должны увидеть страницу результатов, которая обновляется каждый раз, когда вы голосуете. Если вы отправите форму, не выбрав вариант ответа, вы должны увидеть сообщение об ошибке.

```bash
cd ~/project/mysite
python manage.py runserver 0.0.0.0:8080
```

![Poll voting form interface](../assets/20230908-10-37-07-p9ewKbe6.png)

**Примечание:**

В коде нашего представления `vote()` есть небольшая проблема. Он сначала получает объект `selected_choice` из базы данных, затем вычисляет новое значение `votes`, а затем сохраняет его обратно в базу данных. Если два пользователя вашего сайта попытаются проголосовать _ровно одновременно_, это может пойти не так: для `votes` будет получено одно и то же значение, скажем 42. Затем для обоих пользователей вычисляется новое значение 43 и сохраняется, но ожидаемым значением было бы 44.

Это называется _условием гонки_. Если вы заинтересованы, вы можете прочитать статью `avoiding-race-conditions-using-f`, чтобы узнать, как можно решить эту проблему.
