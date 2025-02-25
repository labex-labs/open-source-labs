# Число делится

Напишите функцию `is_divisible(dividend, divisor)`, которая принимает два целых числа в качестве аргументов и возвращает `True`, если `dividend` делится на `divisor`, и `False` в противном случае.

```python
def is_divisible(dividend, divisor):
  return dividend % divisor == 0
```

```python
is_divisible(6, 3) # True
```
