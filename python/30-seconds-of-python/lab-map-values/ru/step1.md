# Преобразование значений словаря

Напишите функцию `map_values(obj, fn)`, которая принимает словарь `obj` и функцию `fn` в качестве аргументов и возвращает новый словарь с теми же ключами, что и исходный словарь, и значениями, сгенерированными путём запуска предоставленной функции для каждого значения.

```python
def map_values(obj, fn):
  return dict((k, fn(v)) for k, v in obj.items())
```

```python
users = {
  'fred': { 'user': 'fred', 'age': 40 },
  'pebbles': { 'user': 'pebbles', 'age': 1 }
}
map_values(users, lambda u : u['age']) # {'fred': 40, 'pebbles': 1}
```
