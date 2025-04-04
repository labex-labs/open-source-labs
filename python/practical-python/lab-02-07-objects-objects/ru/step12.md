# Упражнение 2.25: Создание словарей

Помните, как функция `dict()` может легко создать словарь, если у вас есть последовательность имен ключей и значений? Давайте создадим словарь из имен столбцов:

```python
>>> headers
['name','shares', 'price']
>>> converted
['AA', 100, 32.2]
>>> dict(zip(headers, converted))
{'price': 32.2, 'name': 'AA','shares': 100}
>>>
```

Конечно, если вы хорошо владеете списочными выражениями, вы можете выполнить всю конвертацию за один шаг, используя словарное включение:

```python
>>> { name: func(val) for name, func, val in zip(headers, types, row) }
{'price': 32.2, 'name': 'AA','shares': 100}
>>>
```
