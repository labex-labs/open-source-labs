# Вызов по последовательности Фибоначчи

## Задача

Напишите функцию под названием `fibonacci(n)`, которая принимает целое число `n` в качестве параметра и возвращает список, содержащий последовательность Фибоначчи до n-го члена.

Для решения этой задачи вы можете следовать следующим шагам:

1. Создайте пустой список под названием `sequence`.
2. Если `n` меньше или равно 0, добавьте 0 в список `sequence` и верните список.
3. Добавьте 0 и 1 в список `sequence`.
4. Используйте цикл `while`, чтобы добавить сумму двух последних чисел списка `sequence` в конец списка, пока длина списка не достигнет `n`.
5. Верните список `sequence`.

## Пример

```python
fibonacci(7) # [0, 1, 1, 2, 3, 5, 8, 13]
```
