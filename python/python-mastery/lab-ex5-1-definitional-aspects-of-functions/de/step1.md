# Vorbereitung

In Übung 2.6 haben Sie ein Modul `reader.py` geschrieben, das eine Funktion zum Lesen einer CSV-Datei in eine Liste von Wörterbüchern hatte. Beispielsweise:

```python
>>> import reader
>>> port = reader.read_csv_as_dicts('portfolio.csv', [str,int,float])
>>>
```

Wir haben das Code später erweitert, um mit Instanzen in Übung 3.3 zu arbeiten:

```python
>>> import reader
>>> from stock import Stock
>>> port = reader.read_csv_as_instances('portfolio.csv', Stock)
>>>
```

Schließlich wurde der Code in Übung 3.7 in eine Sammlung von Klassen mit Vererbung umgewandelt. Der Code ist jedoch ziemlich komplex und verwirrt geworden.
