# Преобразование числа в список цифр

Напишите функцию `digitize(n)`, которая принимает неотрицательное целое число `n` в качестве входных данных и возвращает список его цифр. Функция должна выполнить это, выполнив следующие шаги:

1. Преобразуйте входное число `n` в строку.
2. Используйте функцию `map()` в сочетании с функцией `int` для преобразования каждого символа в строке в целое число.
3. Верните полученный список целых чисел.

Например, если входное число равно `123`, функция должна вернуть список `[1, 2, 3]`.

```python
def digitize(n):
  return list(map(int, str(n)))
```

```python
digitize(123) # [1, 2, 3]
```
