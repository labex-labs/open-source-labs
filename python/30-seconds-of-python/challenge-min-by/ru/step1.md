# Найти минимальное значение списка на основе функции

## Задача

Напишите функцию под названием `min_by(lst, fn)`, которая принимает список `lst` и функцию `fn` в качестве аргументов. Функция должна сопоставить каждый элемент списка с значением с использованием предоставленной функции, а затем вернуть минимальное значение.

## Пример

```python
min_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 2
```

В приведенном выше примере функция `min_by()` вызывается с списком словарей и лямбда-функцией, которая извлекает значение ключа `'n'` из каждого словаря. Функция возвращает минимальное значение списка, которое равно `2`.
