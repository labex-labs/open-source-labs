# Изменяемые целые числа

Целые числа в Python обычно неизменяемы. Однако, допустим, вы хотите создать изменяемый объект целого числа. Начните с создания класса следующим образом:

```python
# mutint.py

class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value
```

Попробуйте его:

```python
>>> a = MutInt(3)
>>> a
<__main__.MutInt object at 0x10e79d408>
>>> a.value
3
>>> a.value = 42
>>> a.value
42
>>> a + 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'MutInt' and 'int'
>>>
```

Все это очень интересно, кроме того, что с этим новым объектом `MutInt` ничего не работает должным образом. Печать выглядит ужасно, никакие арифметические операторы не работают, и он по существу является довольно бесполезным. Ну, кроме того, что его значение изменяемое - это, по крайней мере, есть.
