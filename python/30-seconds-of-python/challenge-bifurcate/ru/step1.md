# Разделить список на две части

## Задача

Напишите функцию `bifurcate(lst, filter)`, которая принимает список `lst` и фильтр `filter` в качестве входных данных и возвращает список из двух списков. Первый список должен содержать элементы `lst`, которые проходят фильтр, а второй список - элементы, которые не проходят.

Для реализации этой функции можно использовать списочное выражение и функцию `zip()`. Функция `zip()` принимает два или более списков в качестве входных данных и возвращает список кортежей, где каждый кортеж содержит соответствующие элементы из каждого списка. Например, `zip([1, 2, 3], [4, 5, 6])` возвращает `[(1, 4), (2, 5), (3, 6)]`.

Вы можете использовать эту функцию для одновременного перебора как `lst`, так и `filter` и добавлять элементы в соответствующий список в зависимости от того, проходят они фильтр или нет.

## Пример

```python
bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True])
# Output: [['beep', 'boop', 'bar'], ['foo']]
```

В приведенном выше примере фильтр равен `[True, True, False, True]`. Первые два элемента `lst` проходят фильтр, поэтому они добавляются в первый список. Третий элемент не проходит фильтр, поэтому он добавляется во второй список. Четвертый элемент проходит фильтр, поэтому он добавляется в первый список.
