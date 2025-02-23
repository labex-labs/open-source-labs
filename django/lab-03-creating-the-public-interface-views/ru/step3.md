# Создание представлений, которые действительно что-то делают

Каждое представление отвечает за выполнение одной из двух задач: возвращение объекта `~django.http.HttpResponse`, содержащего содержимое запрошенной страницы, или генерацию исключения, такого как `~django.http.Http404`. Остальное зависит от вас.

Ваш вид может читать записи из базы данных или не читать. Может он использовать систему шаблонов, такую как шаблонизатор Django, или сторонний шаблонизатор на Python, или не использовать. Может он генерировать PDF-файл, выводить XML, создавать ZIP-файл в режиме реального времени - что угодно, используя любые библиотеки Python, которые хотите.

Все, что требуется Django - это `~django.http.HttpResponse`. Или исключение.

Поскольку это удобно, давайте используем собственный API базы данных Django, который мы рассматривали в Уроке 2. Вот попытка создать новый вид `index()`, который отображает последние 5 вопросов опроса в системе, разделенных запятыми, в порядке убывания даты публикации:

Откройте файл `polls/views.py` и измените его так, чтобы он выглядел так:

```python
from django.http import HttpResponse

from.models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


# Оставьте остальные представления (detail, results, vote) без изменений
```

Однако здесь есть проблема: дизайн страницы жестко закодирован в представлении. Если вы хотите изменить внешний вид страницы, вам придется редактировать этот Python-код. Поэтому давайте используем систему шаблонов Django, чтобы отделить дизайн от Python, создав шаблон, который может использовать представление.

Сначала создайте директорию с именем `templates` в директории `polls`. Django будет искать шаблоны в этой директории.

Настройка `TEMPLATES` вашего проекта описывает, как Django будет загружать и отображать шаблоны. Файл настроек по умолчанию настраивает бэкенд `DjangoTemplates`, для которого параметр `APP_DIRS <TEMPLATES-APP_DIRS>` установлен в `True`. По соглашению `DjangoTemplates` ищет поддиректорию "templates" в каждом из `INSTALLED_APPS`.

Внутри директории `templates`, которую вы только что создали, создайте другую директорию с именем `polls`, а внутри нее создайте файл с именем `index.html`. Другими словами, ваш шаблон должен находиться по адресу `polls/templates/polls/index.html`. В силу того, как работает загрузчик шаблонов `app_directories`, описанный выше, вы можете ссылаться на этот шаблон в Django как `polls/index.html`.

## Именование шаблонов

Теперь мы _возможно_ могли бы обойтись без создания дополнительной директории `polls` внутри `polls/templates` (и поместить шаблоны прямо в `polls/templates`), но на самом деле это было бы плохой идеей. Django выберет первый найденный шаблон с совпадающим именем, и если у вас есть шаблон с таким же именем в _другом_ приложении, Django не сможет различить между ними.

Нам нужно уметь указывать Django на правильный шаблон, и лучший способ этого сделать - это _именование_ шаблонов. То есть, поместить эти шаблоны внутри _другой_ директории, названной именем самого приложения.

Вставьте следующий код в этот шаблон:

```html+django
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

Примечание:

Для сокращения урока все примеры шаблонов используют неполный HTML. В своих проектах вы должны использовать [полные HTML-документы](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started#anatomy_of_an_html_document).

Теперь обновим наш вид `index` в `polls/views.py`, чтобы использовать шаблон:

```python
from django.http import HttpResponse
from django.template import loader

from.models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```

Этот код загружает шаблон с именем `polls/index.html` и передает ему контекст. Контекст - это словарь, который сопоставляет имена переменных шаблона объектам Python.

Запустите сервер снова:

```bash
python manage.py runserver 0.0.0.0:8080
```

Откройте страницу, указав в браузере адрес "/polls/", и вы должны увидеть маркированный список, содержащий вопрос "Что нового" из Урока 2. Ссылка ведет на страницу с деталями вопроса.

![Главная страница опросов Django](../assets/20230908-09-37-26-QMKEbUhb.png)

## Короткая запись: `~django.shortcuts.render`

Очень часто используется следующая последовательность действий: загрузить шаблон, заполнить контекст и вернуть объект `~django.http.HttpResponse` с результатом отрендеренного шаблона. Django предоставляет короткую запись для этого. Вот полный вид `index()`, переписанный:

```python
from django.shortcuts import render

from.models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
```

Обратите внимание, что после того, как мы сделали это во всех представлениях, мы больше не нуждаемся в импорте `~django.template.loader` и `~django.http.HttpResponse` (если у вас остались заглушки методов `detail`, `results` и `vote`, вы по-прежнему будете использовать `HttpResponse`).

Функция `~django.shortcuts.render` принимает объект запроса в качестве первого аргумента, имя шаблона в качестве второго аргумента и словарь в качестве необязательного третьего аргумента. Она возвращает объект `~django.http.HttpResponse` с отрендеренным с данным контекстом заданным шаблоном.
