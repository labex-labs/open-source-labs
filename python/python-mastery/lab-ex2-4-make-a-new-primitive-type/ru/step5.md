# Добавление преобразований типов (Type Conversions)

Наш класс `MutInt` в настоящее время поддерживает операции сложения и сравнения. Однако он не работает со встроенными в Python функциями преобразования, такими как `int()` и `float()`. Эти функции преобразования очень полезны в Python. Например, когда вы хотите преобразовать значение в целое число или число с плавающей точкой для различных вычислений или операций, вы полагаетесь на эти функции. Итак, давайте добавим возможности нашему классу `MutInt` для работы с ними.

1. Откройте `mutint.py` в WebIDE и обновите его следующим кодом:

```python
# mutint.py

from functools import total_ordering

@total_ordering
class MutInt:
    """
    Изменяемый класс целых чисел, который позволяет изменять свое значение после создания.
    """
    __slots__ = ['value']

    def __init__(self, value):
        """Инициализация целочисленным значением."""
        self.value = value

    def __str__(self):
        """Возвращает строковое представление для печати."""
        return str(self.value)

    def __repr__(self):
        """Возвращает строковое представление, удобное для разработчиков."""
        return f'MutInt({self.value!r})'

    def __format__(self, fmt):
        """Поддержка форматирования строк со спецификациями формата."""
        return format(self.value, fmt)

    def __add__(self, other):
        """Обработка сложения: self + other."""
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    def __radd__(self, other):
        """Обработка обратного сложения: other + self."""
        return self.__add__(other)

    def __iadd__(self, other):
        """Обработка сложения на месте (in-place addition): self += other."""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented

    def __eq__(self, other):
        """Обработка сравнения на равенство: self == other."""
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        """Обработка сравнения "меньше чем": self < other."""
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    def __int__(self):
        """Преобразование в int (integer)."""
        return self.value

    def __float__(self):
        """Преобразование в float (число с плавающей точкой)."""
        return float(self.value)

    __index__ = __int__  # Поддержка индексации массивов и других операций, требующих индекс

    def __lshift__(self, other):
        """Обработка сдвига влево: self << other."""
        if isinstance(other, MutInt):
            return MutInt(self.value << other.value)
        elif isinstance(other, int):
            return MutInt(self.value << other)
        else:
            return NotImplemented

    def __rlshift__(self, other):
        """Обработка обратного сдвига влево: other << self."""
        if isinstance(other, int):
            return MutInt(other << self.value)
        else:
            return NotImplemented
```

Мы добавили три новых метода в класс `MutInt`:

1. `__int__()`: Этот метод вызывается, когда вы используете функцию `int()` для объекта нашего класса `MutInt`. Например, если у вас есть объект `MutInt` `a`, и вы пишете `int(a)`, Python вызовет метод `__int__()` объекта `a`.
2. `__float__()`: Аналогично, этот метод вызывается, когда вы используете функцию `float()` для нашего объекта `MutInt`.
3. `__index__()`: Этот метод используется для операций, которые специально требуют целочисленный индекс. Например, когда вы хотите получить доступ к элементу в списке, используя индекс, или выполнить операции определения битовой длины (bit-length operations), Python требует целочисленный индекс.
4. `__lshift__()`: Этот метод обрабатывает операции сдвига влево, когда объект `MutInt` находится слева от оператора `<<`.
5. `__rlshift__()`: Этот метод обрабатывает операции сдвига влево, когда объект `MutInt` находится справа от оператора `<<`.

Метод `__index__` имеет решающее значение для операций, требующих целочисленный индекс, таких как индексация списка, срезы (slicing) и операции определения битовой длины. В нашей простой реализации мы устанавливаем его таким же, как `__int__`, потому что значение нашего объекта `MutInt` можно напрямую использовать в качестве целочисленного индекса.

Методы `__lshift__` и `__rlshift__` необходимы для поддержки побитовых операций сдвига влево (bitwise left shift operations). Они позволяют нашим объектам `MutInt` участвовать в побитовых операциях, что является общим требованием для целочисленных типов.

2. Создайте новый тестовый файл с именем `test_conversions.py` для тестирования этих новых методов:

```python
# test_conversions.py

from mutint import MutInt

# Создаем объект MutInt
a = MutInt(3)

# Тестируем преобразования
print(f"int(a): {int(a)}")
print(f"float(a): {float(a)}")

# Тестируем использование в качестве индекса
names = ['Dave', 'Guido', 'Paula', 'Thomas', 'Lewis']
print(f"names[a]: {names[a]}")

# Тестируем использование в битовых операциях (требуется __index__)
print(f"1 << a: {1 << a}")  # Сдвиг влево на 3

# Тестируем функции hex/oct/bin (требуется __index__)
print(f"hex(a): {hex(a)}")
print(f"oct(a): {oct(a)}")
print(f"bin(a): {bin(a)}")

# Изменяем и тестируем снова
a.value = 4
print(f"\nПосле изменения значения на 4:")
print(f"int(a): {int(a)}")
print(f"names[a]: {names[a]}")
```

3. Запустите тестовый скрипт:

```bash
python3 /home/labex/project/test_conversions.py
```

Вы должны увидеть вывод, похожий на этот:

```
int(a): 3
float(a): 3.0
names[a]: Thomas
1 << a: 8
hex(a): 0x3
oct(a): 0o3
bin(a): 0b11

После изменения значения на 4:
int(a): 4
names[a]: Lewis
```

Теперь наш класс `MutInt` можно преобразовать в стандартные типы Python и использовать в операциях, требующих целочисленный индекс.

Метод `__index__` особенно важен. Он был введен в Python, чтобы позволить объектам использоваться в ситуациях, когда требуется целочисленный индекс, таких как индексация списка, побитовые операции и различные функции, такие как `hex()`, `oct()` и `bin()`.

С этими дополнениями наш класс `MutInt` теперь является довольно полным примитивным типом. Его можно использовать в большинстве контекстов, где использовалось бы обычное целое число, с дополнительным преимуществом - изменяемостью.

## Полная реализация MutInt

Вот наша полная реализация `MutInt` со всеми добавленными нами функциями:

```python
# mutint.py

from functools import total_ordering

@total_ordering
class MutInt:
    """
    Изменяемый класс целых чисел, который позволяет изменять свое значение после создания.
    """
    __slots__ = ['value']

    def __init__(self, value):
        """Инициализация целочисленным значением."""
        self.value = value

    def __str__(self):
        """Возвращает строковое представление для печати."""
        return str(self.value)

    def __repr__(self):
        """Возвращает строковое представление, удобное для разработчиков."""
        return f'MutInt({self.value!r})'

    def __format__(self, fmt):
        """Поддержка форматирования строк со спецификациями формата."""
        return format(self.value, fmt)

    def __add__(self, other):
        """Обработка сложения: self + other."""
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    def __radd__(self, other):
        """Обработка обратного сложения: other + self."""
        return self.__add__(other)

    def __iadd__(self, other):
        """Обработка сложения на месте (in-place addition): self += other."""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented

    def __eq__(self, other):
        """Обработка сравнения на равенство: self == other."""
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        """Обработка сравнения "меньше чем": self < other."""
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    def __int__(self):
        """Преобразование в int (integer)."""
        return self.value

    def __float__(self):
        """Преобразование в float (число с плавающей точкой)."""
        return float(self.value)

    __index__ = __int__  # Поддержка индексации массивов и других операций, требующих индекс

    def __lshift__(self, other):
        """Обработка сдвига влево: self << other."""
        if isinstance(other, MutInt):
            return MutInt(self.value << other.value)
        elif isinstance(other, int):
            return MutInt(self.value << other)
        else:
            return NotImplemented

    def __rlshift__(self, other):
        """Обработка обратного сдвига влево: other << self."""
        if isinstance(other, int):
            return MutInt(other << self.value)
        else:
            return NotImplemented
```

Эта реализация охватывает ключевые аспекты создания нового примитивного типа в Python. Чтобы сделать его еще более полным, вы могли бы реализовать дополнительные методы для других операций, таких как вычитание, умножение, деление и т. д.
