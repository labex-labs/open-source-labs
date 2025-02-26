# Реальный декоратор

Совет: Завершите следующее в файле `validate.py`

В упражнении 6.6 вы создали вызываемый класс `ValidatedFunction`, который применял аннотации типов. Перепишите этот класс в виде функции-декоратора под названием `validated`. Это должно позволить вам писать код такого вида:

```python
from validate import Integer, validated

@validated
def add(x: Integer, y:Integer) -> Integer:
    return x + y

@validated
def pow(x: Integer, y:Integer) -> Integer:
    return x ** y
```

Вот, как должны работать декорированные функции:

```python
>>> add(2, 3)
5
>>> add('2', '3')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "validate.py", line 75, in wrapper
    raise TypeError('Bad Arguments\n' + '\n'.join(errors))
TypeError: Bad Arguments
    x: Expected <class 'int'>
    y: Expected <class 'int'>

>>> pow(2, 3)
8
>>> pow(2, -1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "validate.py", line 83, in wrapper
    raise TypeError(f'Bad return: {e}') from None
TypeError: Bad return: Expected <class 'int'>
>>>
```

Ваш декоратор должен пытаться исправить исключения, чтобы они показывали более полезную информацию, как показано выше. Кроме того, декоратор `@validated` должен работать в классах (вам не нужно ничего особенного делать).

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @validated
    def sell(self, nshares:PositiveInteger):
        self.shares -= nshares
```

Примечание: Эта часть не требует написания большого количества кода, но есть много мелких деталей. Решение будет выглядеть почти так же, как и в упражнении 6.6. Не стесняйтесь смотреть на код решения, если нужно.
