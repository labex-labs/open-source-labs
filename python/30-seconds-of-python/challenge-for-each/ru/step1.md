# Выполнить функцию для каждого элемента списка

## Задача

Напишите функцию `for_each(itr, fn)`, которая принимает список `itr` и функцию `fn` в качестве аргументов. Функция должна выполнить `fn` один раз для каждого элемента в `itr`.

## Пример

```python
def print_square(num):
    print(num*num)

for_each([1, 2, 3], print_square) # выводит 1 4 9
```

В приведенном выше примере функция `for_each` вызывается с списком `[1, 2, 3]` и функцией `print_square`. Функция `print_square` выполняется один раз для каждого элемента списка, выводя квадрат каждого числа.
