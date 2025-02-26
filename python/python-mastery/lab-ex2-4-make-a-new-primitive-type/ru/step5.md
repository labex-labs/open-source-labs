# Преобразования

Ваш новый примитивный тип почти готов. Возможно, вы захотите дать ему возможность работать с некоторыми общими преобразованиями. Например:

```python
>>> a = MutInt(3)
>>> int(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: int() argument must be a string, a bytes-like object or a number, not 'MutInt'
>>> float(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: float() argument must be a string, a bytes-like object or a number, not 'MutInt'
>>>
```

Вы можете дать классу методы `__int__()` и `__float__()`, чтобы это исправить:

```python
from functools import total_ordering

@total_ordering
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

...

    def __int__(self):
        return self.value

    def __float__(self):
        return float(self.value)
```

Теперь вы можете правильно преобразовывать:

```python
>>> a = MutInt(3)
>>> int(a)
3
>>> float(a)
3.0
>>>
```

В общем случае Python никогда не автоматически преобразует данные. Таким образом, даже если вы дали классу метод `__int__()`, `MutInt` по-прежнему не будет работать во всех ситуациях, когда ожидается целое число. Например, индексирование:

```python
>>> names = ['Dave', 'Guido', 'Paula', 'Thomas', 'Lewis']
>>> a = MutInt(1)
>>> names[a]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not MutInt
>>>
```

Это можно исправить, дав `MutInt` метод `__index__()`, который возвращает целое число. Измените класс так:

```python
from functools import total_ordering

@total_ordering
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

...

    def __int__(self):
        return self.value

    __index__ = __int__     # Сделать индексирование работоспособным
```

**Обсуждение**

Создание нового примитивного типа данных на самом деле является одним из самых сложных задач программирования в Python. Есть много крайних случаев и низкоуровневых вопросов, о которых нужно беспокоиться - особенно в отношении того, как ваш тип взаимодействует с другими типами Python. Возможно, главное, что нужно牢记, - это то, что вы можете настроить практически каждый аспект взаимодействия объекта с остальной частью Python, если знаете соответствующие протоколы. Если вы собираетесь делать это, рекомендуется изучить существующий код, похожий на то, что вы пытаетесь создать.
