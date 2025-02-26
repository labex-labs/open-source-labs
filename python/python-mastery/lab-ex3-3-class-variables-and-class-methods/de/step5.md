# Verallgemeinerung

Ein nützliches Merkmal von Klassenmethoden ist, dass Sie sie verwenden können, um eine sehr einheitliche Instanzerstellungsoberfläche auf eine Vielzahl von Klassen zu legen und allgemeine Hilfsfunktionen zu schreiben, die diese verwenden.

Früher haben Sie eine Datei `reader.py` erstellt, die einige Funktionen zum Lesen von CSV-Daten hatte. Fügen Sie die folgende `read_csv_as_instances()`-Funktion zur Datei hinzu, die eine Klasse als Eingabe akzeptiert und die `from_row()`-Methode der Klasse verwendet, um eine Liste von Instanzen zu erstellen:

```python
# reader.py
...

def read_csv_as_instances(filename, cls):
    '''
    Liest eine CSV-Datei in eine Liste von Instanzen
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records
```

Entfernen Sie die `read_portfolio()`-Funktion - Sie brauchen sie nicht mehr. Wenn Sie eine Liste von `Stock`-Objekten lesen möchten, tun Sie Folgendes:

```python
>>> # Lese ein Portfolio von Stock-Instanzen
>>> from reader import read_csv_as_instances
>>> from stock import Stock
>>> portfolio = read_csv_as_instances('portfolio.csv', Stock)
>>> portfolio
[<__main__.Stock object at 0x100674748>,
<__main__.Stock object at 0x1006746d8>,
<__main__.Stock object at 0x1006747b8>,
<__main__.Stock object at 0x100674828>,
<__main__.Stock object at 0x100674898>,
<__main__.Stock object at 0x100674908>,
<__main__.Stock object at 0x100674978>]
>>>
```

Hier ist ein weiteres Beispiel, wie Sie `read_csv_as_instances()` mit einer völlig anderen Klasse verwenden könnten:

```python
>>> class Row:
         def __init__(self, route, date, daytype, numrides):
             self.route = route
             self.date = date
             self.daytype = daytype
             self.numrides = numrides
         @classmethod
         def from_row(cls, row):
             return cls(row[0], row[1], row[2], int(row[3]))

>>> rides = read_csv_as_instances('ctabus.csv', Row)
>>> len(rides)
577563
>>>
```

**Diskussion**

Dieses Labor veranschaulicht die zwei am häufigsten verwendeten Anwendungen von Klassenvariablen und Klassenmethoden. Klassenvariablen werden oft verwendet, um einen globalen Parameter (z.B. eine Konfigurationseinstellung) zu speichern, der für alle Instanzen gemeinsam ist. Manchmal werden Unterklassen von der Basisklasse erben und die Einstellung überschreiben, um das Verhalten zu ändern.

Klassenmethoden werden am häufigsten verwendet, um alternative Konstruktoren zu implementieren, wie gezeigt. Ein häufiger Weg, solche Klassenmethoden zu erkennen, ist, nach dem Wort "from" im Namen zu suchen. Beispielsweise ist hier ein Beispiel für die eingebauten Dictionaries:

```python
>>> d = dict.fromkeys(['a','b','c'], 0)     # Klassenmethode
>>> d
{'a': 0, 'c': 0, 'b': 0}
>>>
```
