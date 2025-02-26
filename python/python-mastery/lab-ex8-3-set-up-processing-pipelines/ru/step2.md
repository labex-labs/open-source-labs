# Создайте некоторые компоненты конвейера

В файле `coticker.py` создайте серию компонентов конвейера, которые выполняют те же задачи, что и программа `ticker.py` в упражнении 8.2. Вот реализация различных частей.

```python
# coticker.py
from structure import Structure

class Ticker(Structure):
    name = String()
    price =Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()

from cofollow import consumer, follow
from tableformat import create_formatter
import csv

# Эта часть сложная. См. решение для примечаний по ней
@consumer
def to_csv(target):
    def producer():
        while True:
            yield line

    reader = csv.reader(producer())
    while True:
        line = yield
        target.send(next(reader))

@consumer
def create_ticker(target):
    while True:
        row = yield
        target.send(Ticker.from_row(row))

@consumer
def negchange(target):
    while True:
        record = yield
        if record.change < 0:
            target.send(record)

@consumer
def ticker(fmt, fields):
    formatter = create_formatter(fmt)
    formatter.headings(fields)
    while True:
        rec = yield
        row = [getattr(rec, name) for name in fields]
        formatter.row(row)
```

Ваша задача: Напишите основную программу, которая соединяет все эти компоненты, чтобы сгенерировать тот же тикер акций, что и в предыдущем упражнении.
