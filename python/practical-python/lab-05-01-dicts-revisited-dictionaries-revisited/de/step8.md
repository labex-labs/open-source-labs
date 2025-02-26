# Lesen von Attributen

Nehmen wir an, Sie lesen ein Attribut auf einer Instanz.

```python
x = obj.name
```

Das Attribut kann an zwei Stellen vorhanden sein:

- Lokales Instanzwörterbuch.
- Klassenwörterbuch.

Beide Wörterbücher müssen überprüft werden. Zunächst wird im lokalen `__dict__` nachgeschaut. Wenn es nicht gefunden wird, wird im `__dict__` der Klasse über `__class__` gesucht.

```python
>>> s = Stock(...)
>>> s.name
'GOOG'
>>> s.cost()
49010.0
>>>
```

Dieses Suchschema ist die Art und Weise, wie die Mitglieder einer _Klasse_ von allen Instanzen geteilt werden.
