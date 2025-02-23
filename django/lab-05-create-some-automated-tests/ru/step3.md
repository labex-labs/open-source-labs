# Написание нашего первого теста

## Мы выявляем ошибку

К счастью, в приложении `polls` есть небольшая ошибка, которую мы можем исправить сразу: метод `Question.was_published_recently()` возвращает `True`, если `Question` была опубликована в течение последнего дня (что верно), но также если поле `pub_date` `Question` находится в будущем (что, конечно, не так).

Подтвердите ошибку, используя `shell`, чтобы проверить метод на вопросе, дата которого находится в будущем:

```bash
cd ~/project/mysite
python manage.py shell
```

```python
>>> import datetime
>>> from django.utils import timezone
>>> from polls.models import Question
>>> # создаем экземпляр Question с pub_date через 30 дней
>>> future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
>>> # была ли она опубликована недавно?
>>> future_question.was_published_recently()
True
```

Поскольку вещи в будущем не являются "недавними", это явно неправильно.

## Создаем тест, чтобы выявить ошибку

То, что мы только что сделали в `shell` для тестирования проблемы, это то, что мы можем сделать в автоматическом тесте, поэтому давайте превратим это в автоматический тест.

Конвенциональное место для тестов приложения - это файл `tests.py` приложения; тестирующая система автоматически найдет тесты в любом файле, имя которого начинается с `test`.

Вставьте следующее в файл `tests.py` в приложении `polls`:

```python
import datetime

from django.test import TestCase
from django.utils import timezone

from.models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() возвращает False для вопросов, у которых pub_date
        находится в будущем.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
```

Здесь мы создали подкласс `django.test.TestCase` с методом, который создает экземпляр `Question` с `pub_date` в будущем. Затем мы проверяем вывод `was_published_recently()` - который, _должен_ быть `False`.

## Запуск тестов

В терминале мы можем запустить наш тест:

```bash
python manage.py test polls
```

и вы увидите что-то вроде:

```shell
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F
======================================================================
FAIL: test_was_published_recently_with_future_question (polls.tests.QuestionModelTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/path/to/mysite/polls/tests.py", line 16, in test_was_published_recently_with_future_question
    self.assertIs(future_question.was_published_recently(), False)
AssertionError: True is not False

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
Destroying test database for alias 'default'...
```

> Различая ошибка?

Если вместо этого у вас возникает `NameError`, вы, возможно, пропустили шаг в `Часть 2 <tutorial02-import-timezone>`, где мы добавили импорты `datetime` и `timezone` в `polls/models.py`. Скопируйте импорты из этого раздела и попробуйте запустить тесты снова.

Что произошло:

- `manage.py test polls` искала тесты в приложении `polls`
- она нашла подкласс класса `django.test.TestCase`
- она создала специальную базу данных для тестирования
- она искала тестовые методы - те, имена которых начинаются с `test`
- в `test_was_published_recently_with_future_question` она создала экземпляр `Question`, у которого поле `pub_date` находится на 30 дней в будущем
  -... и, используя метод `assertIs()`, она обнаружила, что его `was_published_recently()` возвращает `True`, хотя мы хотели, чтобы он возвращал `False`

Тест сообщает нам, какой тест не пройден, и даже строку, на которой произошла ошибка.

## Исправление ошибки

Мы уже знаем, что проблема: `Question.was_published_recently()` должен возвращать `False`, если его `pub_date` находится в будущем. Отредактируйте метод в `models.py`, чтобы он возвращал `True` только если дата также находится в прошлом:

```python
def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now
```

и запустите тест снова:

```bash
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
Destroying test database for alias 'default'...
```

После выявления ошибки мы написали тест, который ее выявляет, и исправили ошибку в коде, чтобы наш тест прошел.

В будущем с нашим приложением могут возникнуть многие другие проблемы, но мы можем быть уверены, что мы не случайно не снова внедрим эту ошибку, потому что запуск теста немедленно предупредит нас. Мы можем считать этот маленький кусок приложения надежно закрепленным навсегда.

## Более полные тесты

Пока мы здесь, мы можем еще более точно определить метод `was_published_recently()`; на самом деле, было бы весьма стыдно, если в исправлении одной ошибки мы бы ввели другую.

Добавьте еще два тестовых метода в ту же класс, чтобы более полно протестировать поведение метода:

```python
def test_was_published_recently_with_old_question(self):
    """
    was_published_recently() возвращает False для вопросов, у которых pub_date
    старше 1 дня.
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_question = Question(pub_date=time)
    self.assertIs(old_question.was_published_recently(), False)


def test_was_published_recently_with_recent_question(self):
    """
    was_published_recently() возвращает True для вопросов, у которых pub_date
    находится в течение последнего дня.
    """
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_question = Question(pub_date=time)
    self.assertIs(recent_question.was_published_recently(), True)
```

И теперь у нас есть три теста, которые подтверждают, что `Question.was_published_recently()` возвращает разумные значения для вопросов в прошлом, недавнем и будущем.

Опять же, `polls` - это минимальное приложение, но как бы сложным оно ни стало в будущем и с кем бы оно ни взаимодействовало, мы теперь имеем гарантию, что метод, для которого мы написали тесты, будет работать ожидаемым образом.
