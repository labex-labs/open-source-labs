# Construye algunos componentes de la tubería

En un archivo `coticker.py`, construye una serie de componentes de la tubería que realicen las mismas tareas que el programa `ticker.py` del Ejercicio 8.2. Aquí está la implementación de las diferentes partes.

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

# Esta es complicada. Ver la solución para notas al respecto
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

Tu desafío: Escribe el programa principal que enlace todos estos componentes para generar el mismo cotizador de acciones que en el ejercicio anterior.
