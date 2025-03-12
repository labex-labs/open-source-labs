# Создание вспомогательного класса с типизацией структуры

На этом этапе мы создадим более практичный пример. Реализуем функцию, которая создает классы с валидацией типов. Валидация типов имеет важное значение, так как она гарантирует, что данные, присваиваемые атрибутам класса, соответствуют определенным критериям, например, являются определенным типом данных или находятся в определенном диапазоне. Это помогает выявлять ошибки на ранней стадии и делает наш код более надежным.

## Понимание класса Structure

Сначала нам нужно открыть файл `structure.py` в редакторе WebIDE. Этот файл содержит базовый класс `Structure`. Этот класс предоставляет основную функциональность для инициализации и представления структурированных объектов. Инициализация означает настройку объекта с предоставленными данными, а представление - это то, как объект отображается при его выводе.

Для открытия файла используем следующую команду в терминале:

```bash
cd ~/project
```

После выполнения этой команды вы окажетесь в правильной директории, где находится файл `structure.py`. При открытии файла вы увидите базовый класс `Structure`. Наша цель - расширить этот класс для поддержки валидации типов.

## Реализация функции typed_structure

Теперь добавим функцию `typed_structure` в файл `structure.py`. Эта функция создаст новый класс, который наследуется от класса `Structure` и включает указанные валидаторы. Наследование означает, что новый класс будет иметь всю функциональность класса `Structure` и также может добавить свои собственные особенности. Валидаторы используются для проверки, являются ли значения, присваиваемые атрибутам класса, допустимыми.

Вот код функции `typed_structure`:

```python
def typed_structure(clsname, **validators):
    """
    Create a Structure class with type validation.

    Parameters:
    - clsname: Name of the class to create
    - validators: Keyword arguments mapping attribute names to validator objects

    Returns:
    - A new class with the specified name and validators
    """
    cls = type(clsname, (Structure,), validators)
    return cls
```

Параметр `clsname` - это имя, которое мы хотим дать новому классу. Параметр `validators` - это словарь, где ключи - это имена атрибутов, а значения - это объекты валидаторов. Функция `type()` используется для динамического создания нового класса. Она принимает три аргумента: имя класса, кортеж базовых классов (в данном случае только класс `Structure`) и словарь атрибутов класса (валидаторы).

После добавления этой функции ваш файл `structure.py` должен выглядеть следующим образом:

```python
# Structure class definition

class Structure:
    _fields = ()

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')

        # Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the remaining keyword arguments
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __repr__(self):
        attrs = ', '.join(f'{name}={getattr(self, name)!r}' for name in self._fields)
        return f'{type(self).__name__}({attrs})'

def typed_structure(clsname, **validators):
    """
    Create a Structure class with type validation.

    Parameters:
    - clsname: Name of the class to create
    - validators: Keyword arguments mapping attribute names to validator objects

    Returns:
    - A new class with the specified name and validators
    """
    cls = type(clsname, (Structure,), validators)
    return cls
```

## Тестирование функции typed_structure

Протестируем нашу функцию `typed_structure` с использованием валидаторов из файла `validate.py`. Эти валидаторы используются для проверки, являются ли значения, присваиваемые атрибутам класса, правильного типа и соответствуют ли другим критериям.

Сначала откройте интерактивную оболочку Python. Используем следующие команды в терминале:

```bash
cd ~/project
python3
```

Первая команда переводит нас в правильную директорию, а вторая команда запускает интерактивную оболочку Python.

Теперь импортируем необходимые компоненты и создаем структуру с типизацией:

```python
from validate import String, PositiveInteger, PositiveFloat
from structure import typed_structure

# Create a Stock class with type validation
Stock = typed_structure('Stock', name=String(), shares=PositiveInteger(), price=PositiveFloat())

# Create a stock instance
s = Stock('GOOG', 100, 490.1)

# Test the instance
print(s.name)
print(s)

# Test validation
try:
    invalid_stock = Stock('AAPL', -10, 150.25)  # Should raise an error
except ValueError as e:
    print(f"Validation error: {e}")
```

Мы импортируем валидаторы `String`, `PositiveInteger` и `PositiveFloat` из файла `validate.py`. Затем используем функцию `typed_structure` для создания класса `Stock` с валидацией типов. Создаем экземпляр класса `Stock` и тестируем его, выводя его атрибуты. Наконец, пытаемся создать недопустимый экземпляр акции, чтобы протестировать валидацию.

Вы должны увидеть вывод, похожий на следующий:

```
GOOG
Stock('GOOG', 100, 490.1)
Validation error: Expected a positive value
```

После завершения тестирования выйдите из оболочки Python:

```python
exit()
```

Этот пример демонстрирует, как можно использовать функцию `type()` для создания пользовательских классов с определенными правилами валидации. Этот подход очень мощный, так как позволяет программно генерировать классы, что может сэкономить много времени и сделать наш код более гибким.
