# Задача на нахождение n максимальных элементов

## Проблема

Напишите функцию `max_n(lst, n = 1)`, которая принимает список `lst` и необязательный целый аргумент `n` и возвращает список из `n` максимальных элементов из данного списка. Если аргумент `n` не указан, функция должна вернуть список, содержащий максимальный элемент списка. Если `n` больше или равно длине списка, функция должна вернуть исходный список, отсортированный в порядке убывания.

Ваша задача - реализовать функцию `max_n()`.

## Пример

```python
max_n([1, 2, 3]) # [3]
max_n([1, 2, 3], 2) # [3, 2]
max_n([1, 2, 3, 4, 5], 3) # [5, 4, 3]
max_n([1, 2, 3, 4, 5], 6) # [5, 4, 3, 2, 1]
```
