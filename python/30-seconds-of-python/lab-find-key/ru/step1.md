# Найти ключ по значению в словаре

Напишите функцию `find_key(dict, val)`, которая находит первый ключ в предоставленном словаре, имеющий заданное значение.

Ваша функция должна:

- Принимать словарь `dict` и значение `val` в качестве входных данных.
- Использовать `dictionary.items()` и `next()` для возврата первого ключа, значение которого равно `val`.
- Возвращать ключ в качестве результата.

```python
def find_key(dict, val):
  return next(key for key, value in dict.items() if value == val)
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
find_key(ages, 11) # 'Isabel'
```
