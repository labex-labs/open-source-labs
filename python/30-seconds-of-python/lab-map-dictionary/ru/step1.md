# Преобразование списка в словарь

Напишите функцию на Python с именем `map_dictionary(itr, fn)`, которая принимает два параметра:

- `itr`: список значений
- `fn`: функция, которая принимает значение на вход и возвращает значение на выход

Функция должна вернуть словарь (dictionary), в котором пары ключ-значение состоят из исходного значения в качестве ключа и результата выполнения функции в качестве значения.

Для решения этой задачи следуйте этим шагам:

1. Используйте `map()`, чтобы применить `fn` к каждому значению списка.
2. Используйте `zip()`, чтобы соединить исходные значения с значениями, полученными в результате применения `fn`.
3. Используйте `dict()`, чтобы вернуть соответствующий словарь.

```python
def map_dictionary(itr, fn):
  return dict(zip(itr, map(fn, itr)))
```

```python
map_dictionary([1, 2, 3], lambda x: x * x) # { 1: 1, 2: 4, 3: 9 }
```
