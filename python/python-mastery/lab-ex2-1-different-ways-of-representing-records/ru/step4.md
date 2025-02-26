# Затраты памяти на другие структуры данных

В Python есть множество различных вариантов представления структур данных. Например:

```python
# Кортеж
row = (route, date, daytype, rides)

# Словарь
row = {
    'route': route,
    'date': date,
    'daytype': daytype,
    'rides': rides,
}

# Класс
class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

# Именованный кортеж
from collections import namedtuple
Row = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])

# Класс с __slots__
class Row:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides
```

Ваша задача следующая: создайте разные версии функции `read_rides()`, которые используют каждую из этих структур данных для представления одной строки данных. Затем определите затраты памяти каждого варианта. Выясните, какой подход обеспечивает наиболее эффективное хранение, если вы работаете с большим объемом данных сразу.
