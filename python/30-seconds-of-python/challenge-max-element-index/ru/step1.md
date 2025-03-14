# Индекс максимального элемента

## Задача

Напишите функцию `max_element_index(arr)`, которая принимает список `arr` в качестве аргумента и возвращает индекс элемента с максимальным значением. Если есть несколько элементов с максимальным значением, верните индекс первого вхождения.

Для решения этой задачи вы можете следовать следующим шагам:

1. Используйте встроенную функцию `max()` для нахождения максимального значения в списке.
2. Используйте встроенную функцию `list.index()` для нахождения индекса первого вхождения максимального значения в списке.
3. Верните индекс.

## Пример

```python
max_element_index([5, 8, 9, 7, 10, 3, 0]) # 4
```

В этом примере максимальное значение в списке `[5, 8, 9, 7, 10, 3, 0]` равно `10`, которое находится по индексу `4`. Поэтому функция должна вернуть `4`.
