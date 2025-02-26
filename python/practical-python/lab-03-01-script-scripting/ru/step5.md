# Что такое функция?

Функция - это именованная последовательность инструкций.

```python
def funcname(args):
  statement
  statement
...
  return result
```

_Любая_ инструкция Python может использоваться внутри.

```python
def foo():
    import math
    print(math.sqrt(2))
    help(math)
```

В Python нет _особенных_ инструкций (что делает ее легкой для запоминания).
