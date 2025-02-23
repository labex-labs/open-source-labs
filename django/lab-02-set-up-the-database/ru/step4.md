# Изучаем API

Теперь давайте займемся в интерактивной оболочке Python и поэкспериментируем с бесплатным API, которое предоставляет Django. Чтобы вызвать Python-оболочку, используйте эту команду:

```bash
python manage.py shell
```

Мы используем ее вместо простого ввода "python", потому что `manage.py` устанавливает переменную окружения `DJANGO_SETTINGS_MODULE`, которая дает Django путь к импорту Python в ваш файл `mysite/settings.py`.

Как только вы в оболочке, изучите `API базы данных </topics/db/queries>`:

```python
>>> from polls.models import Choice, Question  # Импортируем классы моделей, которые только что написали.

# В системе еще нет вопросов.
>>> Question.objects.all()
<QuerySet []>

# Создаем новый вопрос.
# В настройках по умолчанию включена поддержка часовых поясов, поэтому
# Django ожидает datetime с tzinfo для pub_date. Используйте timezone.now()
# вместо datetime.datetime.now() и все будет в порядке.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# Сохраняем объект в базу данных. Нужно явно вызвать save().
>>> q.save()

# Теперь у него есть ID.
>>> q.id
1

# Доступ к значениям полей модели через атрибуты Python.
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2023, 9, 7, 1, 18, 48, 335644, tzinfo=datetime.timezone.utc)

# Меняем значения, изменяя атрибуты, а затем вызываем save().
>>> q.question_text = "What's up?"
>>> q.save()

# objects.all() отображает все вопросы в базе данных.
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>
```

Подождите минутку. `<Question: Question object (1)>` не очень информативное представление этого объекта. Исправим это, отредактировав модель `Question` (в файле `polls/models.py`) и добавив метод `~django.db.models.Model.__str__` как для `Question`, так и для `Choice`:

```python
from django.db import models


class Question(models.Model):
    #...
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    #...
    def __str__(self):
        return self.choice_text
```

Важно добавить методы `~django.db.models.Model.__str__` к вашим моделям, не только для вашего удобства при работе с интерактивной командной строкой, но и потому, что представления объектов используются повсюду в автоматически создаваемом административном интерфейсе Django.

Давайте также добавим к этой модели пользовательский метод:

```python
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    #...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
```

Обратите внимание на добавление `import datetime` и `from django.utils import timezone`, чтобы ссылаться на стандартный модуль `datetime` Python и утилиты Django, связанные с часовыми поясами, в `django.utils.timezone` соответственно. Если вы не знакомы с обработкой часовых поясов в Python, вы можете узнать больше в `документации по поддержке часовых поясов </topics/i18n/timezones>`.

Сохраните эти изменения и запустите новую Python-интерактивную оболочку, **запустив `python manage.py shell` снова**:

```python
>>> from polls.models import Choice, Question

# Убедимся, что наша добавка к __str__() сработала.
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>

# Django предоставляет богатое API для поиска в базе данных, которое полностью управляется
# ключевыми аргументами.
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
>>> Question.objects.filter(question_text__startswith="What")
<QuerySet [<Question: What's up?>]>

# Получаем вопрос, опубликованный в этом году.
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

# Запрашиваем ID, который не существует, это вызовет исключение.
>>> Question.objects.get(id=2)
Traceback (most recent call last):
 ...
DoesNotExist: Question matching query does not exist.

# Поиск по первичному ключу - это наиболее распространенный случай, поэтому Django предоставляет
# быстрый способ для точного поиска по первичному ключу.
# Следующая строка эквивалентна Question.objects.get(id=1).
>>> Question.objects.get(pk=1)
<Question: What's up?>

# Убедимся, что наша пользовательская функция сработала.
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# Добавим несколько вариантов ответа для вопроса. Вызов create() создает новый
# объект Choice, выполняет оператор INSERT, добавляет вариант ответа в набор
# доступных вариантов и возвращает новый объект Choice. Django создает
# набор для хранения "другой стороны" отношения ForeignKey
# (например, варианты ответа для вопроса), который можно получить через API.
>>> q = Question.objects.get(pk=1)

# Отобразим все варианты ответа из связанного набора объектов - пока их нет.
>>> q.choice_set.all()
<QuerySet []>

# Создадим три варианта ответа.
>>> q.choice_set.create(choice_text="Not much", votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text="The sky", votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text="Just hacking again", votes=0)

# Объекты Choice имеют API-доступ к их связанным объектам Question.
>>> c.question
<Question: What's up?>

# И наоборот: объекты Question получают доступ к объектам Choice.
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3

# API автоматически следит за связями столько, сколько вам нужно.
# Используйте двойные нижние подчеркивания, чтобы разделить связи.
# Это работает на любом уровне вложенности, который вы хотите; ограничений нет.
# Найдем все варианты ответа для любого вопроса, у которого pub_date
# попадает в этот год (переиспользуем переменную 'current_year', которую мы создали выше).
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# Удалим один из вариантов ответа. Используем для этого delete().
>>> c = q.choice_set.filter(choice_text__startswith="Just hacking")
>>> c.delete()
```

Для получения более подробной информации о связях моделей см. `Доступ к связанным объектам </ref/models/relations>`. Для более подробного описания того, как использовать двойные нижние подчеркивания для выполнения поиска по полям через API, см. `Поиск по полям <field-lookups-intro>`. Для полной информации о API базы данных см. наш `Справочник по API базы данных </topics/db/queries>`.
