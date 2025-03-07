# Ключи словаря

Напишите функцию `keys_only(flat_dict)`, которая принимает на вход плоский словарь и возвращает список всех его ключей.

Для решения этой проблемы вы можете следовать следующим шагам:

1. Используйте `dict.keys()`, чтобы вернуть ключи в заданном словаре.
2. Верните `list()` предыдущего результата.

```python
def keys_only(flat_dict):
  return list(flat_dict.keys())
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
keys_only(ages) # ['Peter', 'Isabel', 'Anna']
```
