# Вызов на нахождение среднего значения

## Задача

Напишите функцию под названием `average`, которая принимает два или более чисел и возвращает их среднее значение. Ваша функция должна соответствовать следующим принципам:

- Используйте `sum()`, чтобы сложить все переданные `args`, а затем разделить на `len()`.
- Функция должна быть способна обрабатывать любое количество аргументов.
- Функция должна возвращать вещественное число (float).

## Пример

```python
average(*[1, 2, 3]) # 2.0
average(1, 2, 3) # 2.0
```
