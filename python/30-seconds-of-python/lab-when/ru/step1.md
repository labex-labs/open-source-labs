# Применить функцию, когда условие истинно

Напишите функцию под названием `when`, которая принимает два аргумента: функцию предиката `predicate` и функцию для применения `when_true`. Функция `when` должна возвращать новую функцию, которая принимает один аргумент `x`. Новая функция должна проверить, является ли значение `predicate(x)` истинным. Если это так, новая функция должна вызвать `when_true(x)` и вернуть результат. В противном случае новая функция должна вернуть `x`.

```python
def when(predicate, when_true):
  return lambda x: when_true(x) if predicate(x) else x
```

```python
double_even_numbers = when(lambda x: x % 2 == 0, lambda x : x * 2)
double_even_numbers(2) # 4
double_even_numbers(1) # 1
```
