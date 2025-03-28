# Найти выбросы четности

## Задача

Напишите функцию `find_parity_outliers(nums)`, которая принимает список целых чисел `nums` в качестве аргумента и возвращает список всех выбросов четности в `nums`.

Для решения этой задачи вы можете следовать следующим шагам:

1. Используйте `collections.Counter` с генератором списка для подсчета четных и нечетных значений в списке.
2. Используйте `collections.Counter.most_common()`, чтобы получить наиболее часто встречающуюся четность.
3. Используйте генератор списка, чтобы найти все элементы, которые не соответствуют наиболее часто встречающейся четности.

## Пример

```python
find_parity_outliers([1, 2, 3, 4, 6]) # [1, 3]
```

В приведенном выше примере большинство элементов в списке четные, поэтому выбросами четности являются нечетные элементы 1 и 3.
