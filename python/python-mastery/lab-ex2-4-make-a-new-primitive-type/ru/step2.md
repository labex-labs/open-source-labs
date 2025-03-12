# Улучшение строкового представления

Когда вы выводите объект `MutInt` в Python, вы увидите такой вывод, как `<__main__.MutInt object at 0x...>`. Этот вывод не очень полезен, так как он не сообщает вам фактическое значение объекта `MutInt`. Чтобы сделать более понятным, что представляет собой объект, мы реализуем специальные методы для строкового представления.

1. Откройте файл `mutint.py` в WebIDE и обновите его следующим кодом:

```python
# mutint.py

class MutInt:
    """
    A mutable integer class that allows its value to be modified after creation.
    """
    __slots__ = ['value']

    def __init__(self, value):
        """Initialize with an integer value."""
        self.value = value

    def __str__(self):
        """Return a string representation for printing."""
        return str(self.value)

    def __repr__(self):
        """Return a developer-friendly string representation."""
        return f'MutInt({self.value!r})'

    def __format__(self, fmt):
        """Support string formatting with format specifications."""
        return format(self.value, fmt)
```

Мы добавили три важных метода в класс `MutInt`:

- `__str__()`: Этот метод вызывается, когда вы используете функцию `str()` на объекте или когда вы напрямую выводите объект. Он должен возвращать человекочитаемую строку.
- `__repr__()`: Этот метод предоставляет "официальное" строковое представление объекта. Он в основном используется для отладки и, желательно, должен возвращать строку, которая, если передать в функцию `eval()`, воссоздаст объект.
- `__format__()`: Этот метод позволяет использовать систему форматирования строк Python с объектами `MutInt`. Вы можете использовать спецификации форматирования, такие как выравнивание и форматирование чисел.

2. Создайте новый тестовый файл с именем `test_string_repr.py` для тестирования этих новых методов:

```python
# test_string_repr.py

from mutint import MutInt

# Create a MutInt object
a = MutInt(3)

# Test string representation
print(f"str(a): {str(a)}")
print(f"repr(a): {repr(a)}")

# Test direct printing
print(f"Print a: {a}")

# Test string formatting
print(f"Formatted with padding: '{a:*^10}'")
print(f"Formatted as decimal: '{a:d}'")

# Test mutability
a.value = 42
print(f"After changing value, repr(a): {repr(a)}")
```

В этом тестовом файле мы сначала импортируем класс `MutInt`. Затем создаем объект `MutInt` со значением `3`. Мы тестируем методы `__str__()` и `__repr__()` с помощью функций `str()` и `repr()`. Мы также тестируем прямой вывод, форматирование строк и изменяемость объекта `MutInt`.

3. Запустите тестовый скрипт:

```bash
python3 /home/labex/project/test_string_repr.py
```

Когда вы выполните эту команду, Python выполнит скрипт `test_string_repr.py`. Вы должны увидеть вывод, похожий на следующий:

```
str(a): 3
repr(a): MutInt(3)
Print a: 3
Formatted with padding: '****3*****'
Formatted as decimal: '3'
After changing value, repr(a): MutInt(42)
```

Теперь наши объекты `MutInt` выводятся красиво. Строковое представление показывает базовое значение, и мы можем использовать форматирование строк, как и с обычными целыми числами.

Разница между `__str__()` и `__repr__()` заключается в том, что `__str__()` предназначен для создания человекочитаемого вывода, в то время как `__repr__()` должен, желательно, создавать строку, которая, когда передается в `eval()`, воссоздает объект. Именно поэтому мы включили имя класса в метод `__repr__()`.

Метод `__format__()` позволяет нашему объекту работать с системой форматирования Python, поэтому мы можем использовать спецификации форматирования, такие как выравнивание и форматирование чисел.
