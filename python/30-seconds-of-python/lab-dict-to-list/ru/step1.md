# Словарь в список

Напишите функцию `dict_to_list(d)`, которая принимает словарь `d` в качестве аргумента и возвращает список кортежей. Каждый кортеж должен содержать пару ключ-значение из словаря. Порядок кортежей в списке должен совпадать с порядком пар ключ-значение в словаре.

```python
def dict_to_list(d):
  return list(d.items())
```

```python
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
dict_to_list(d)
# [('one', 1), ('three', 3), ('five', 5), ('two', 2), ('four', 4)]
```
