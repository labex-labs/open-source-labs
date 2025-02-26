# Передача кортежей и словарей

Кортежи можно расширять в переменные аргументы.

```python
numbers = (2,3,4)
f(1, *numbers)      # То же, что и f(1,2,3,4)
```

Словари также можно расширять в ключевые аргументы.

```python
options = {
    'color' : 'red',
    'delimiter' : ',',
    'width' : 400
}
f(data, **options)
# То же, что и f(data, color='red', delimiter=',', width=400)
```
