# Ключевые переменные аргументы (\*\*kwargs)

Функция также может принимать любое количество ключевых аргументов. Например:

```python
def f(x, y, **kwargs):
 ...
```

Вызов функции.

```python
f(2, 3, flag=True, mode='fast', header='debug')
```

Дополнительные ключевые слова передаются в виде словаря.

```python
def f(x, y, **kwargs):
    # x -> 2
    # y -> 3
    # kwargs -> { 'flag': True,'mode': 'fast', 'header': 'debug' }
```
