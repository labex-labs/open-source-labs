# Найти последний совпадающий индекс

## Задача

Напишите функцию `find_last_index(lst, fn)`, которая принимает список `lst` и функцию `fn` в качестве аргументов. Функция должна возвращать индекс последнего элемента в `lst`, для которого `fn` возвращает `True`. Если ни один элемент не удовлетворяет условию, функция должна возвращать `-1`.

## Пример

```python
find_last_index([1, 2, 3, 4], lambda n: n % 2 == 1) # 2
find_last_index([2, 4, 6, 8], lambda n: n % 2 == 1) # -1
```
