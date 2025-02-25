# Наибольший общий делитель

Напишите функцию под названием `gcd(numbers)`, которая принимает список целых чисел в качестве аргумента и возвращает их наибольший общий делитель. Ваша функция должна использовать `functools.reduce()` и `math.gcd()` для заданного списка.

```python
from functools import reduce
from math import gcd as _gcd

def gcd(numbers):
  return reduce(_gcd, numbers)
```

```python
gcd([8, 36, 28]) # 4
```
