# Проверить, существует ли ключ в словаре

Напишите функцию `key_in_dict(d, key)`, которая принимает словарь `d` и ключ `key` в качестве аргументов и возвращает `True`, если ключ существует в словаре, и `False` в противном случае.

```python
def key_in_dict(d, key):
  return (key in d)
```

```python
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
key_in_dict(d, 'three') # True
```
