# Часть 1: Числа

Арифметические вычисления в Python работают так, как вы ожидаете. Например:

```python
>>> 3 + 4*5
23
>>> 23.45 / 1e-02
2345.0
>>>
```

Обратите внимание, что целочисленное деление в Python 2 и Python 3 различается.

```python
>>> 7 / 4      # В Python 2 это округляет до 1
1.75
>>> 7 // 4     # Отбрасывающее деление
1
>>>
```

Если вы хотите поведение Python 3 в Python 2, сделайте следующее:

```python
>>> from __future__ import division
>>> 7 / 4
1.75
>>> 7 // 4      # Отбрасывающее деление
1
>>>
```

Числа имеют небольшой набор методов, многие из которых относительно недавние и могут быть пропущены даже опытными программистами на Python. Попробуйте некоторые из них.

```python
>>> x = 1172.5
>>> x.as_integer_ratio()
(2345, 2)
>>> x.is_integer()
False
>>> y = 12345
>>> y.numerator
12345
>>> y.denominator
1
>>> y.bit_length()
14
>>>
```
