# Создание системы валидации с использованием наследования

В этом шаге мы создадим практическую систему валидации с использованием наследования. Наследование - это мощная концепция в программировании, которая позволяет создавать новые классы на основе существующих. Таким образом, вы можете повторно использовать код и создавать более организованные и модульные программы. Создав эту систему валидации, вы увидите, как наследование можно использовать для создания переиспользуемых компонентов кода, которые можно комбинировать различными способами.

## Создание базового класса валидатора

Сначала нам нужно создать базовый класс для наших валидаторов. Для этого создадим новый файл в WebIDE. Вот как вы можете сделать это: кликните на "File" > "New File", или вы можете использовать сочетание клавиш. После открытия нового файла назовите его `validate.py`.

Теперь добавим некоторый код в этот файл, чтобы создать базовый класс `Validator`. Этот класс будет служить основой для всех наших других валидаторов.

```python
# validate.py
class Validator:
    @classmethod
    def check(cls, value):
        return value
```

В этом коде мы определили класс `Validator` с методом `check`. Метод `check` принимает значение в качестве аргумента и просто возвращает его без изменений. Декоратор `@classmethod` используется, чтобы сделать этот метод методом класса. Это означает, что мы можем вызывать этот метод на самом классе, не создавая экземпляр класса.

## Добавление валидаторов типов

Далее мы добавим несколько валидаторов, которые проверяют тип значения. Эти валидаторы будут наследовать от класса `Validator`, который мы только что создали. Вернитесь к файлу `validate.py` и добавьте следующий код:

```python
class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return super().check(value)

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str
```

Класс `Typed` является подклассом `Validator`. Он имеет атрибут `expected_type`, который изначально установлен на `object`. Метод `check` в классе `Typed` проверяет, является ли данное значение ожидаемого типа. Если это не так, он вызывает исключение `TypeError`. Если тип правильный, он вызывает метод `check` родительского класса с помощью `super().check(value)`.

Классы `Integer`, `Float` и `String` наследуются от `Typed` и указывают точный тип, который они должны проверять. Например, класс `Integer` проверяет, является ли значение целым числом.

## Тестирование валидаторов типов

Теперь, когда мы создали наши валидаторы типов, давайте протестируем их. Откройте новый терминал и запустите интерпретатор Python, выполнив следующую команду:

```bash
python3
```

После запуска интерпретатора Python мы можем импортировать и протестировать наши валидаторы. Вот некоторый код для их тестирования:

```python
from validate import Integer, String

Integer.check(10)  # Should return 10

try:
    Integer.check('10')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")

String.check('10')  # Should return '10'
```

При выполнении этого кода вы должны увидеть что-то вроде этого:

```
10
Error: Expected <class 'int'>
'10'
```

Мы также можем использовать эти валидаторы в функции. Давайте попробуем это:

```python
def add(x, y):
    Integer.check(x)
    Integer.check(y)
    return x + y

add(2, 2)  # Should return 4

try:
    add('2', '3')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")
```

При выполнении этого кода вы должны увидеть:

```
4
Error: Expected <class 'int'>
```

## Добавление валидаторов значений

До сих пор мы создали валидаторы, которые проверяют тип значения. Теперь добавим несколько валидаторов, которые проверяют само значение, а не его тип. Вернитесь к файлу `validate.py` и добавьте следующий код:

```python
class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        return super().check(value)

class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('Must be non-empty')
        return super().check(value)
```

Валидатор `Positive` проверяет, является ли значение неотрицательным. Если значение меньше 0, он вызывает исключение `ValueError`. Валидатор `NonEmpty` проверяет, имеет ли значение ненулевую длину. Если длина равна 0, он вызывает исключение `ValueError`.

## Компоновка валидаторов с использованием множественного наследования

Теперь мы объединим наши валидаторы с использованием множественного наследования. Множественное наследование позволяет классу наследовать от более чем одного родительского класса. Вернитесь к файлу `validate.py` и добавьте следующий код:

```python
class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass
```

Эти новые классы объединяют проверку типа и проверку значения. Например, класс `PositiveInteger` проверяет, что значение является целым числом и неотрицательным. Здесь порядок наследования имеет значение. Валидаторы проверяются в порядке, указанном в определении класса.

## Тестирование составных валидаторов

Давайте протестируем наши составные валидаторы. В интерпретаторе Python выполните следующий код:

```python
from validate import PositiveInteger, PositiveFloat, NonEmptyString

PositiveInteger.check(10)  # Should return 10

try:
    PositiveInteger.check('10')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")

try:
    PositiveInteger.check(-10)  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")

NonEmptyString.check('hello')  # Should return 'hello'

try:
    NonEmptyString.check('')  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")
```

При выполнении этого кода вы должны увидеть:

```
10
Error: Expected <class 'int'>
Error: Expected >= 0
'hello'
Error: Must be non-empty
```

Это показывает, как мы можем комбинировать валидаторы, чтобы создать более сложные правила валидации.

После завершения тестирования вы можете выйти из интерпретатора Python, выполнив следующую команду:

```python
exit()
```
