# Vorbereitung

Im letzten Übungsaufgabe haben Sie eine Klasse `Structure` erstellt, die es einfacher machte, Datenstrukturen zu definieren. Beispielsweise:

```python
class Stock(Structure):
    _fields = ('name','shares','price')
```

Dies funktioniert gut, außer dass es viele Dinge an der `__init__()`-Funktion ziemlich seltsam macht. Beispielsweise erhalten Sie keine nützliche Signatur, wenn Sie `help(Stock)` verwenden, um Hilfe zu erhalten. Auch funktioniert das Übergeben von Schlüsselwortargumenten nicht. Beispielsweise:

```python
>>> help(Stock)
... schauen Sie sich die Ausgabe an...

>>> s = Stock(name='GOOG', shares=100, price=490.1)
Fehler (letzter Aufruf zuletzt):
  Datei "<stdin>", Zeile 1, in <modul>
TypeError: __init__() erhielt ein unerwartetes Schlüsselwortargument 'price'
>>>
```

In dieser Übung werden wir einen anderen Ansatz für das Problem betrachten.
