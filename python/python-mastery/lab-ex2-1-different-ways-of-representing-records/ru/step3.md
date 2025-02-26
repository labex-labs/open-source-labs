# Список кортежей

На практике вы можете прочитать данные в список и преобразовать каждую строку в какую - то другую структуру данных. Вот программа `readrides.py`, которая читает весь файл в список кортежей с использованием модуля `csv`:

```python
# readrides.py

import csv

def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_rides_as_tuples('/home/labex/project/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
```

Запустите эту программу с использованием `python3 -i readrides.py` и посмотрите на полученные содержимое `rows`. Вы должны получить список кортежей такого вида:

```python
>>> len(rows)
577563
>>> rows[0]
('3', '01/01/2001', 'U', 7354)
>>> rows[1]
('4', '01/01/2001', 'U', 9288)
```

Посмотрите на полученное использование памяти. Оно должно быть значительно выше, чем в шаге 2.
