# Тестирование представления

Приложение для опросов довольно недискриминантно: оно публикует любые вопросы, включая те, у которых поле `pub_date` находится в будущем. Мы должны это исправить. Установка `pub_date` в будущем должна означать, что вопрос будет опубликован в тот момент, но будет невидимым до этого времени.

## Тест для представления

Когда мы исправляли ошибку выше, мы сначала написали тест, а затем код для ее исправления. Фактически это был пример разработки по тестированию, но порядок выполнения работы на самом деле не имеет особого значения.

В нашем первом тесте мы тщательно сосредоточились на внутреннем поведении кода. Для этого теста мы хотим проверить его поведение, как оно будет воспринято пользователем через веб-браузер.

Прежде чем пытаться что-то исправить, давайте посмотрим на инструменты, которые у нас есть.

## Тестовый клиент Django

Django предоставляет тестовый `~django.test.Client` для имитации взаимодействия пользователя с кодом на уровне представления. Мы можем использовать его в `tests.py` или даже в `shell`.

Мы начнем снова с `shell`, где нам нужно сделать несколько вещей, которые не понадобятся в `tests.py`. Первое - это настройка тестовой среды в `shell`:

```bash
python manage.py shell
```

```python
>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()
```

`~django.test.utils.setup_test_environment` устанавливает рендер шаблонов, который позволит нам изучить некоторые дополнительные атрибуты в ответах, такие как `response.context`, которые иначе не будут доступны. Обратите внимание, что этот метод _не_ настраивает тестовую базу данных, поэтому следующее будет выполняться на основе существующей базы данных, и вывод может отличаться в зависимости от вопросов, которые вы уже создали. Вы можете получить непредвиденные результаты, если ваш `TIME_ZONE` в `settings.py` не правильный. Если вы не помните, назначили ли его ранее, проверьте его перед продолжением.

Далее нам нужно импортировать класс тестового клиента (позже в `tests.py` мы будем использовать класс `django.test.TestCase`, который自带自己的 клиент, поэтому этого не понадобится):

```python
>>> from django.test import Client
>>> # создаем экземпляр клиента для нашего использования
>>> client = Client()
```

С этим готовым, мы можем попросить клиента сделать для нас какую-то работу:

```python
>>> # получаем ответ от '/'
>>> response = client.get("/")
Not Found: /
>>> # мы должны ожидать 404 от этого адреса; если вместо этого вы видите
>>> # ошибку "Invalid HTTP_HOST header" и ответ 400, вы, вероятно,
>>> # опустили вызов setup_test_environment() описанный выше.
>>> response.status_code
404
>>> # с другой стороны, мы должны ожидать найти что-то по адресу '/polls/'
>>> # мы будем использовать'reverse()' вместо жестко заданного URL
>>> from django.urls import reverse
>>> response = client.get(reverse("polls:index"))
>>> response.status_code
200
>>> response.content
b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#x27;s up?</a></li>\n    \n    </ul>\n\n'
>>> response.context["latest_question_list"]
<QuerySet [<Question: What's up?>]>
```

## Улучшение нашего представления

Список опросов показывает опросы, которые еще не опубликованы (то есть те, у которых `pub_date` находится в будущем). Давайте это исправим.

В `**Обработка форм и сокращение нашего кода**` мы ввели представление на основе класса, основанного на `~django.views.generic.list.ListView`:

```python
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]
```

Мы должны изменить метод `get_queryset()` и сделать его так, чтобы он также проверял дату, сравнивая ее с `timezone.now()`. Сначала нам нужно добавить импорт:

```python
from django.utils import timezone
```

а затем мы должны изменить метод `get_queryset` так:

```python
def get_queryset(self):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
        :5
    ]
```

`Question.objects.filter(pub_date__lte=timezone.now())` возвращает queryset, содержащий `Question`, у которых `pub_date` меньше или равно - то есть раньше или равно - `timezone.now`.

## Тестирование нашего нового представления

Теперь вы можете убедиться, что это работает как ожидается, запустив `runserver`, загрузив сайт в своем браузере, создав `Questions` с датами в прошлом и будущем, и проверив, что в списке отображаются только опубликованные. Вы не хотите каждый раз делать это, когда вы вносите любые изменения, которые могут повлиять на это - поэтому давайте также создадим тест на основе нашей `shell`-сессии выше.

Добавьте следующее в `polls/tests.py`:

```python
from django.urls import reverse
```

и мы создадим функцию-укладчик для создания вопросов, а также новый класс тестов:

```python
def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question2, question1],
        )
```

Давайте более внимательно рассмотрим некоторые из них.

Первое - это функция-укладчик вопросов, `create_question`, чтобы избавиться от некоторой повторяемости в процессе создания вопросов.

`test_no_questions` не создает никаких вопросов, но проверяет сообщение: "No polls are available." и подтверждает, что `latest_question_list` пустой. Обратите внимание, что класс `django.test.TestCase`提供了一些额外的断言方法。在这些示例中，我们使用了 `~django.test.SimpleTestCase.assertContains()` 和 `~django.test.TransactionTestCase.assertQuerySetEqual()`。

В `test_past_question` мы создаем вопрос и проверяем, что он отображается в списке.

В `test_future_question` мы создаем вопрос с `pub_date` в будущем. База данных сбрасывается для каждого тестового метода, поэтому первый вопрос уже не там, и поэтому снова на главной странице не должно быть никаких вопросов.

И так далее. По сути, мы используем тесты, чтобы рассказать историю о вводе администратора и пользовательском опыте на сайте, и проверяем, что на каждом этапе и для каждого нового изменения состояния системы выводятся ожидаемые результаты.

## Тестирование `DetailView`

То, что у нас работает хорошо; однако, хотя будущие вопросы не отображаются на _главной странице_, пользователи все еще могут получить к ним доступ, если знают или угадают правильный URL. Поэтому мы должны добавить аналогичное ограничение для `DetailView`:

```python
class DetailView(generic.DetailView):
  ...

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
```

Затем мы должны добавить несколько тестов, чтобы проверить, что `Question`, у которого `pub_date` находится в прошлом, может быть отображен, а с `pub_date` в будущем - нет:

```python
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text="Future question.", days=5)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text="Past Question.", days=-5)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
```

## Идеи для дополнительных тестов

Мы должны добавить аналогичный метод `get_queryset` в `ResultsView` и создать новый класс тестов для этого представления. Это будет очень похоже на то, что мы только что создали; на самом деле будет много повторений.

Мы также можем улучшить наше приложение по другим путям, добавляя тесты по ходу работы. Например, глупо, что на сайте могут быть опубликованы `Questions`, которые не имеют `Choices`. Поэтому наши представления могут проверить это и исключить такие `Questions`. Наши тесты создадут `Question` без `Choices` и затем проверить, что он не опубликован, а также создадут аналогичный `Question` _с_ `Choices` и проверить, что он _опубликован_.

Возможно, авторизованные администраторы должны иметь возможность видеть неопубликованные `Questions`, но не обычные посетители. Опять же: все, что нужно добавить в программное обеспечение, чтобы это сделать, должно сопровождаться тестом, будь то написание теста сначала и затем заставление кода проходить тест, или выработка логики в коде сначала и затем написание теста, чтобы доказать ее.

В определенный момент вы, безусловно, будете смотреть на свои тесты и задавать себе вопрос, не страдает ли ваш код от избыточности тестов, что приводит нас к:
