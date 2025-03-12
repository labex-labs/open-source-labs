# Сбор типов валидаторов

В Python валидаторы - это классы, которые помогают нам убедиться, что данные соответствуют определенным критериям. Наша первая задача в этом эксперименте - модифицировать базовый класс `Validator` так, чтобы он мог собрать все его подклассы. Почему нам это нужно? Ну, собирая все подклассы валидаторов, мы можем создать пространство имен, которое содержит все типы валидаторов. Позже мы внедрим это пространство имен в класс `Structure`, что облегчит нам управление и использование различных валидаторов.

Теперь давайте начнем работать с кодом. Откройте файл `validate.py`. Вы можете использовать следующую команду в терминале, чтобы открыть его:

```bash
code validate.py
```

После того, как файл открыт, нам нужно добавить словарь на уровне класса и метод `__init_subclass__()` в класс `Validator`. Словарь на уровне класса будет использоваться для хранения всех подклассов валидаторов, а метод `__init_subclass__()` - это специальный метод в Python, который вызывается каждый раз, когда определяется подкласс текущего класса.

Добавьте следующий код в класс `Validator` сразу после определения класса:

```python
# Add this to the Validator class in validate.py
validators = {}  # Dictionary to collect all validator subclasses

@classmethod
def __init_subclass__(cls):
    """Register each validator subclass in the validators dictionary"""
    Validator.validators[cls.__name__] = cls
```

После добавления кода ваш модифицированный класс `Validator` должен выглядеть следующим образом:

```python
class Validator:
    validators = {}  # Dictionary to collect all validator subclasses

    @classmethod
    def __init_subclass__(cls):
        """Register each validator subclass in the validators dictionary"""
        Validator.validators[cls.__name__] = cls

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.name] = value

    def validate(self, value):
        pass
```

Теперь каждый раз, когда определяется новый тип валидатора, например `String` или `PositiveInteger`, Python автоматически вызовет метод `__init_subclass__()`. Этот метод затем добавит новый подкласс валидатора в словарь `validators`, используя имя класса в качестве ключа.

Давайте проверим, работает ли наш код. Мы создадим простой скрипт Python, чтобы проверить содержимое словаря `validators`. Вы можете выполнить следующую команду в терминале:

```bash
python3 -c "from validate import Validator; print(Validator.validators)"
```

Если все работает правильно, вы должны увидеть вывод, похожий на следующий, показывающий все типы валидаторов и соответствующие им классы:

```
{'Typed': <class 'validate.Typed'>, 'Positive': <class 'validate.Positive'>, 'NonEmpty': <class 'validate.NonEmpty'>, 'String': <class 'validate.String'>, 'Integer': <class 'validate.Integer'>, 'Float': <class 'validate.Float'>, 'PositiveInteger': <class 'validate.PositiveInteger'>, 'PositiveFloat': <class 'validate.PositiveFloat'>, 'NonEmptyString': <class 'validate.NonEmptyString'>}
```

Теперь, когда у нас есть словарь, содержащий все наши типы валидаторов, мы можем использовать его на следующем шаге для создания нашего метакласса.
