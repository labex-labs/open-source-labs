# Отсортировать словарь по ключу

Напишите функцию `sort_dict_by_key(d, reverse=False)`, которая принимает словарь `d` и возвращает новый отсортированный по ключу словарь. Функция должна иметь необязательный параметр `reverse`, который по умолчанию равен `False`. Если `reverse` равен `True`, словарь должен быть отсортирован в обратном порядке.

```python
def sort_dict_by_key(d, reverse = False):
  return dict(sorted(d.items(), reverse = reverse))
```

```python
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
sort_dict_by_key(d) # {'five': 5, 'four': 4, 'one': 1, 'three': 3, 'two': 2}
sort_dict_by_key(d, True)
# {'two': 2, 'three': 3, 'one': 1, 'four': 4, 'five': 5}
```
