# Объединение словарей

Напишите функцию `merge_dictionaries(*dicts)`, которая принимает два или более словарей в качестве аргументов и возвращает новый словарь, содержащий все пары ключ-значение из входных словарей.

Ваша функция должна создавать новый словарь и перебирать входные словари, используя `dictionary.update()`, чтобы добавить пары ключ-значение из каждого словаря в результат.

```python
def merge_dictionaries(*dicts):
  res = dict()
  for d in dicts:
    res.update(d)
  return res
```

```python
ages_one = {
  'Peter': 10,
  'Isabel': 11,
}
ages_two = {
  'Anna': 9
}
merge_dictionaries(ages_one, ages_two)
# { 'Peter': 10, 'Isabel': 11, 'Anna': 9 }
```
