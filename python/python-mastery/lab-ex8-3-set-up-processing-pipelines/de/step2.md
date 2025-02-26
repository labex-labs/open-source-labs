# Baue einige Pipeline-Komponenten

In einer Datei `coticker.py` erstelle eine Reihe von Pipeline-Komponenten, die die gleichen Aufgaben wie das Programm `ticker.py` im Übungsblatt 8.2 ausführen. Hier ist die Implementierung der verschiedenen Teile.

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

# Dies ist tricky. Siehe Lösung für Notizen dazu
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

Ihre Herausforderung: Schreiben Sie das Hauptprogramm, das alle diese Komponenten zusammenhängt, um den gleichen Aktien-Ticker wie im vorherigen Übungsblatt zu generieren.
