# Список частичных сумм

## Задача

Напишите функцию `partial_sum(lst)`, которая принимает список чисел в качестве аргумента и возвращает список частичных сумм. Ваша функция должна выполнять следующие шаги:

1. Используйте `itertools.accumulate()`, чтобы создать накопительную сумму для каждого элемента в списке.
2. Используйте `list()`, чтобы преобразовать результат в список.
3. Верните список частичных сумм.

## Пример

```python
partial_sum([1, 2, 3, 4, 5]) # [1, 3, 6, 10, 15]
partial_sum([2, 4, 6, 8, 10]) # [2, 6, 12, 20, 30]
partial_sum([5, 10, 15, 20, 25]) # [5, 15, 30, 50, 75]
```
