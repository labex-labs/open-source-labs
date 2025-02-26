# Collections

В модуле `collections` есть различные классы для более специализированной манипуляции данными. Например, последний пример можно было бы решить с использованием `Counter` так:

```python
>>> from collections import Counter
>>> totals = Counter()
>>> for s in portfolio:
        totals[s['name']] += s['shares']

>>> totals
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
>>>
```

`Counter` интересны тем, что они поддерживают другие виды операций, такие как ранжирование и математика. Например:

```python
>>> # Получить два наиболее часто встречающихся элемента
>>> totals.most_common(2)
[('MSFT', 250), ('IBM', 150)]
>>>

>>> # Сложение счетчиков
>>> more = Counter()
>>> more['IBM'] = 75
>>> more['AA'] = 200
>>> more['ACME'] = 30
>>> more
Counter({'AA': 200, 'IBM': 75, 'ACME': 30})
>>> totals
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
>>> totals + more
Counter({'AA': 300, 'MSFT': 250, 'IBM': 225, 'CAT': 150, 'GE': 95, 'ACME': 30})
>>>
```

Объект `defaultdict` можно использовать для группировки данных. Например, предположим, что вы хотите легко найти все соответствующие записи для заданного имени, такого как IBM. Попробуйте это:

```python
>>> from collections import defaultdict
>>> byname = defaultdict(list)
>>> for s in portfolio:
        byname[s['name']].append(s)

>>> byname['IBM']
[{'name': 'IBM','shares': 50, 'price': 91.1}, {'name': 'IBM','shares': 100, 'price': 70.44}]
>>> byname['AA']
[{'name': 'AA','shares': 100, 'price': 32.2}]
>>>
```

Основная особенность, которая позволяет это сделать, заключается в том, что `defaultdict` автоматически инициализирует элементы для вас, позволяя комбинировать вставку нового элемента и операцию `append()`.
