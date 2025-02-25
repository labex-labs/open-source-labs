# Объединить списки

Напишите функцию под названием `merge(*args, fill_value=None)`, которая принимает два или более списков в качестве аргументов и возвращает список списков. Функция должна объединять элементы из каждого входного списка на основе их позиций. Если список короче самого длинного списка, функция должна использовать `fill_value` для оставшихся элементов. Если `fill_value` не указан, по умолчанию должно быть `None`.

Ваша задача — реализовать функцию `merge()`.

```python
def merge(*args, fill_value = None):
  max_length = max([len(lst) for lst in args])
  result = []
  for i in range(max_length):
    result.append([
      args[k][i] if i < len(args[k]) else fill_value for k in range(len(args))
    ])
  return result
```

```python
merge(['a', 'b'], [1, 2], [True, False]) # [['a', 1, True], ['b', 2, False]]
merge(['a'], [1, 2], [True, False]) # [['a', 1, True], [None, 2, False]]
merge(['a'], [1, 2], [True, False], fill_value = '_')
# [['a', 1, True], ['_', 2, False]]
```
