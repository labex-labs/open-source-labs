# Мощность множества

Напишите функцию на Python под названием `powerset(iterable)`, которая принимает итерируемый объект в качестве аргумента и возвращает мощность этого итерируемого объекта. Функция должна выполнять следующие шаги:

1. Преобразовать заданное значение в список.
2. Использовать `range()` и `itertools.combinations()` для создания генератора, который возвращает все подмножества.
3. Использовать `itertools.chain.from_iterable()` и `list()`, чтобы обработать генератор и вернуть список.

```python
from itertools import chain, combinations

def powerset(iterable):
  s = list(iterable)
  return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
```

```python
powerset([1, 2]) # [(), (1,), (2,), (1, 2)]
```
