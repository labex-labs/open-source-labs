# Добавление математических операций

В настоящее время наш класс `MutInt` не поддерживает математические операции, такие как сложение. В Python, чтобы включить такие операции для пользовательского класса, нам нужно реализовать специальные методы. Эти специальные методы также известны как "магические методы" или "дандер-методы", так как они окружены двойными подчеркиваниями. Давайте добавим функциональность сложения, реализовав соответствующие специальные методы для арифметических операций.

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
        # For commutative operations like +, we can reuse __add__
        return self.__add__(other)

    def __iadd__(self, other):
        """Handle in-place addition: self += other."""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented
```

Мы добавили три новых метода в класс `MutInt`:

- `__add__()`: Этот метод вызывается, когда оператор `+` используется с нашим объектом `MutInt` слева. Внутри этого метода мы сначала проверяем, является ли операнд `other` экземпляром `MutInt` или `int`. Если это так, мы выполняем сложение и возвращаем новый объект `MutInt` с результатом. Если операнд `other` является чем-то другим, мы возвращаем `NotImplemented`. Это сообщает Python попробовать другие методы или вызвать `TypeError`.
- `__radd__()`: Этот метод вызывается, когда оператор `+` используется с нашим объектом `MutInt` справа. Поскольку сложение является коммутативной операцией (т.е. `a + b` равно `b + a`), мы можем просто повторно использовать метод `__add__`.
- `__iadd__()`: Этот метод вызывается, когда оператор `+=` используется с нашим объектом `MutInt`. Вместо создания нового объекта он модифицирует существующий объект `MutInt` и возвращает его.

2. Создайте новый тестовый файл с именем `test_math_ops.py` для тестирования этих новых методов:

```python
# test_math_ops.py

from mutint import MutInt

# Create MutInt objects
a = MutInt(3)
b = MutInt(5)

# Test regular addition
c = a + b
print(f"a + b = {c}")

# Test addition with int
d = a + 10
print(f"a + 10 = {d}")

# Test reversed addition
e = 7 + a
print(f"7 + a = {e}")

# Test in-place addition
print(f"Before a += 5: a = {a}")
a += 5
print(f"After a += 5: a = {a}")

# Test in-place addition with reference sharing
f = a  # f and a point to the same object
print(f"Before a += 10: a = {a}, f = {f}")
a += 10
print(f"After a += 10: a = {a}, f = {f}")

# Test unsupported operation
try:
    result = a + 3.5  # Adding a float is not supported
    print(f"a + 3.5 = {result}")
except TypeError as e:
    print(f"Error when adding float: {e}")
```

В этом тестовом файле мы сначала импортируем класс `MutInt`. Затем мы создаем несколько объектов `MutInt` и выполняем различные типы операций сложения. Мы также тестируем операцию сложения на месте и случай, когда выполняется неподдерживаемая операция (сложение с числом с плавающей точкой).

3. Запустите тестовый скрипт:

```bash
python3 /home/labex/project/test_math_ops.py
```

Вы должны увидеть вывод, похожий на следующий:

```
a + b = MutInt(8)
a + 10 = MutInt(13)
7 + a = MutInt(10)
Before a += 5: a = MutInt(3)
After a += 5: a = MutInt(8)
Before a += 10: a = MutInt(8), f = MutInt(8)
After a += 10: a = MutInt(18), f = MutInt(18)
Error when adding float: unsupported operand type(s) for +: 'MutInt' and 'float'
```

Теперь наш класс `MutInt` поддерживает базовые операции сложения. Обратите внимание, что когда мы использовали `+=`, и `a`, и `f` были обновлены. Это показывает, что `a += 10` модифицировал существующий объект, а не создал новый.

Это поведение с изменяемыми объектами аналогично встроенным изменяемым типам Python, таким как списки. Например:

```python
a = [1, 2, 3]
b = a
a += [4, 5]  # Both a and b are updated
```

В отличие от этого, для неизменяемых типов, таких как кортежи, `+=` создает новый объект:

```python
c = (1, 2, 3)
d = c
c += (4, 5)  # c is a new object, d still points to the old one
```
