# Создание пользовательского контейнера - Великий обман

Сохранение данных в столбцах обеспечивает гораздо более эффективное использование памяти, но данные теперь сложнее обрабатывать. Фактически, никакой из нашего раннего анализирующего кода из упражнения 2.2 не может работать с данными в столбцах. Причина, по которой все сломалось, заключается в том, что вы нарушили абстракцию данных, использованную в предыдущих упражнениях - а именно предположение, что данные хранятся в виде списка словарей.

Это можно исправить, если вы готовы создать пользовательский объект-контейнер, который будет "подделывать" это. Давайте сделаем это.

Ранее написанный анализирующий код предполагает, что данные хранятся в последовательности записей. Каждая запись представлена в виде словаря. Давайте начнем с создания нового класса "Sequence". В этом классе мы будем хранить четыре столбца данных, которые использовались в функции `read_rides_as_columns()`.

```python
# readrides.py

from collections.abc import Sequence

...

class RideData(Sequence):
    def __init__(self):
        self.routes = []      # Columns
        self.dates = []
        self.daytypes = []
        self.numrides = []
```

Попробуйте создать экземпляр `RideData`. Вы обнаружите, что это завершится ошибкой с сообщением об ошибке такого вида:

```python
>>> records = RideData()
Traceback (most recent call last):
...
TypeError: Can't instantiate abstract class RideData with abstract methods __getitem__, __len__
>>>
```

Внимательно прочитайте сообщение об ошибке. Он говорит нам, что нужно реализовать. Добавим методы `__len__()` и `__getitem__()`. В методе `__getitem__()` мы создадим словарь. Кроме того, мы создадим метод `append()`, который будет принимать словарь и распаковывать его в четыре отдельных операции `append()`.

```python
# readrides.py
...

class RideData(collections.Sequence):
    def __init__(self):
        # Each value is a list with all of the values (a column)
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        # All lists assumed to have the same length
        return len(self.routes)

    def __getitem__(self, index):
        return { 'route': self.routes[index],
                 'date': self.dates[index],
                 'daytype': self.daytypes[index],
                 'rides': self.numrides[index] }

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])
```

Если вы сделали это правильно, вы должны быть в состоянии передать этот объект в ранее написанную функцию `read_rides_as_dicts()`. Для этого нужно изменить только одну строку кода:

```python
# readrides.py
...

def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of dicts
    '''
    records = RideData()      # <--- CHANGE THIS
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides' : rides
                }
            records.append(record)
    return records
```

Если вы сделали все правильно, старый код должен работать точно так же, как и раньше. Например:

```python
>>> rows = readrides.read_rides_as_dicts('ctabus.csv')
>>> rows
<readrides.RideData object at 0x10f5054a8>
>>> len(rows)
577563
>>> rows[0]
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
>>> rows[1]
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
>>> rows[2]
{'route': '6', 'date': '01/01/2001', 'daytype': 'U', 'rides': 6048}
>>>
```

Запустите ранее написанный код CTA из упражнения 2.2. Он должен работать без изменений, но использовать значительно меньше памяти.
