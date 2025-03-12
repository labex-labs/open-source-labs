# Добавление преобразований типов

Наша класс `MutInt` в настоящее время поддерживает операции сложения и сравнения. Однако он не работает с встроенными функциями преобразования Python, такими как `int()` и `float()`. Эти функции преобразования очень полезны в Python. Например, когда вы хотите преобразовать значение в целое число или число с плавающей точкой для различных вычислений или операций, вы используете эти функции. Поэтому давайте добавим в наш класс `MutInt` возможность работать с ними.

1. Откройте файл `mutint.py` в WebIDE и обновите его следующим кодом:

```python
# mutint.py

from functools import total_ordering

@total_ordering
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
        """Return a developer - friendly string representation."""
        return f'MutInt({self.value!r})'

    def __format__(self, fmt):
        """Support string formatting with format specifications."""
        return format(self.value, fmt)

    def __add__(self, other):
        """Handle addition: self + other."""
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    def __radd__(self, other):
        """Handle reversed addition: other + self."""
        return self.__add__(other)

    def __iadd__(self, other):
        """Handle in - place addition: self += other."""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented

    def __eq__(self, other):
        """Handle equality comparison: self == other."""
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        """Handle less - than comparison: self < other."""
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    def __int__(self):
        """Convert to int."""
        return self.value

    def __float__(self):
        """Convert to float."""
        return float(self.value)

    __index__ = __int__  # Support array indexing and other operations requiring an index
```

Мы добавили три новых метода в класс `MutInt`:

1. `__int__()`: Этот метод вызывается, когда вы используете функцию `int()` на объекте нашего класса `MutInt`. Например, если у вас есть объект `MutInt` с именем `a`, и вы пишете `int(a)`, Python вызовет метод `__int__()` объекта `a`.
2. `__float__()`: Аналогично, этот метод вызывается, когда вы используете функцию `float()` на объекте `MutInt`.
3. `__index__()`: Этот метод используется для операций, которые требуют целочисленного индекса. Например, когда вы хотите получить доступ к элементу в списке по индексу или выполнить операции с битовой длиной, Python требует целочисленного индекса.

Метод `__index__` является важным для операций, которые требуют целочисленного индекса, таких как индексация списка, срезка и операции с битовой длиной. В нашей простой реализации мы установили его равным `__int__`, так как значение нашего объекта `MutInt` может быть напрямую использовано как целочисленный индекс.

2. Создайте новый тестовый файл с именем `test_conversions.py` для тестирования этих новых методов:

```python
# test_conversions.py

from mutint import MutInt

# Create a MutInt object
a = MutInt(3)

# Test conversions
print(f"int(a): {int(a)}")
print(f"float(a): {float(a)}")

# Test using as an index
names = ['Dave', 'Guido', 'Paula', 'Thomas', 'Lewis']
print(f"names[a]: {names[a]}")

# Test using in bit operations (requires __index__)
print(f"1 << a: {1 << a}")  # Shift left by 3

# Test hex/oct/bin functions (requires __index__)
print(f"hex(a): {hex(a)}")
print(f"oct(a): {oct(a)}")
print(f"bin(a): {bin(a)}")

# Modify and test again
a.value = 5
print(f"\nAfter changing value to 5:")
print(f"int(a): {int(a)}")
print(f"names[a]: {names[a]}")
```

3. Запустите тестовый скрипт:

```bash
python3 /home/labex/project/test_conversions.py
```

Вы должны увидеть вывод, похожий на следующий:

```
int(a): 3
float(a): 3.0
names[a]: Paula
1 << a: 8
hex(a): 0x3
oct(a): 0o3
bin(a): 0b11

After changing value to 5:
int(a): 5
names[a]: Lewis
```

Теперь наш класс `MutInt` может быть преобразован в стандартные типы Python и использован в операциях, которые требуют целочисленного индекса.

Метод `__index__` особенно важен. Он был введен в Python, чтобы позволить объектам использоваться в ситуациях, где требуется целочисленный индекс, таких как индексация списка, битовые операции и различные функции, такие как `hex()`, `oct()` и `bin()`.

Благодаря этим добавлениям наш класс `MutInt` теперь представляет собой довольно полноценный примитивный тип. Он может быть использован в большинстве контекстов, где используется обычное целое число, с дополнительным преимуществом быть изменяемым.

## Полная реализация MutInt

Вот наша полная реализация `MutInt` со всеми добавленными функциями:

```python
# mutint.py

from functools import total_ordering

@total_ordering
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
        """Return a developer - friendly string representation."""
        return f'MutInt({self.value!r})'

    def __format__(self, fmt):
        """Support string formatting with format specifications."""
        return format(self.value, fmt)

    def __add__(self, other):
        """Handle addition: self + other."""
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    def __radd__(self, other):
        """Handle reversed addition: other + self."""
        return self.__add__(other)

    def __iadd__(self, other):
        """Handle in - place addition: self += other."""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented

    def __eq__(self, other):
        """Handle equality comparison: self == other."""
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        """Handle less - than comparison: self < other."""
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    def __int__(self):
        """Convert to int."""
        return self.value

    def __float__(self):
        """Convert to float."""
        return float(self.value)

    __index__ = __int__  # Support array indexing and other operations requiring an index
```

Эта реализация охватывает ключевые аспекты создания нового примитивного типа в Python. Чтобы сделать его еще более полноценным, вы можете реализовать дополнительные методы для других операций, таких как вычитание, умножение, деление и т.д.
