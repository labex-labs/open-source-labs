# Объединение списков на основе функции

## Задача

Напишите функцию `union_by(a, b, fn)`, которая принимает два списка `a` и `b` и функцию `fn`. Функция должна возвращать список, содержащий каждый элемент, который есть в любом из двух списков один раз, после применения предоставленной функции к каждому элементу обоих.

Для решения этой задачи вы можете следовать следующим шагам:

1. Создайте `множество`, применяя `fn` к каждому элементу в `a`.
2. Используйте генератор списка в сочетании с `fn` для `b`, чтобы оставить только значения, не содержащиеся в ранее созданном множестве, `_a`.
3. Наконец, создайте `множество` из предыдущего результата и `a` и преобразуйте его в `список`.

Функция должна иметь следующие входные параметры:

- `a`: список элементов
- `b`: список элементов
- `fn`: функция, которая принимает элемент и возвращает значение

Функция должна возвращать список элементов.

## Пример

Вот пример того, что должна делать `union_by()`:

```python
from math import floor

union_by([2.1], [1.2, 2.3], floor) # [2.1, 1.2]
```

В этом примере `union_by()` принимает два списка `[2.1]` и `[1.2, 2.3]` и функцию `floor()`. Функция применяет `floor()` к каждому элементу обоих списков, создавая множество `{2}`. Затем она использует генератор списка, чтобы оставить только значения, не содержащиеся в множестве, то есть `[1.2]`. Наконец, она создает множество из предыдущего результата и `[2.1]`, то есть `{1.2, 2.1}`, и преобразует его в список `[1.2, 2.1]`.
