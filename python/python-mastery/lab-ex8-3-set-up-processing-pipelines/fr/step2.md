# Créez quelques composants de pipeline

Dans un fichier `coticker.py`, construisez une série de composants de pipeline qui effectuent les mêmes tâches que le programme `ticker.py` de l'exercice 8.2. Voici l'implémentation des différents morceaux.

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

# Celui-ci est difficile. Consultez la solution pour les notes à ce sujet
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

Votre défi : Écrivez le programme principal qui relie tous ces composants pour générer le même fil d'actualité boursière que dans l'exercice précédent.
