# Die Rolle von Klassen

Die Definitionen, die eine Klassendefinition ausmachen, werden von allen Instanzen dieser Klasse geteilt. Beachten Sie, dass alle Instanzen einen Link zu ihrer zugehörigen Klasse haben:

```python
>>> goog.__class__
... schauen Sie sich das Ergebnis an...
>>> ibm.__class__
... schauen Sie sich das Ergebnis an...
>>>
```

Versuchen Sie, eine Methode auf den Instanzen aufzurufen:

```python
>>> goog.cost()
49010.0
>>> ibm.cost()
4561.5
>>>
```

Beachten Sie, dass der Name 'cost' weder in `goog.__dict__` noch in `ibm.__dict__` definiert ist. Stattdessen wird er aus dem Klassenwörterbuch geliefert. Versuchen Sie das:

```python
>>> SimpleStock.__dict__['cost']
... schauen Sie sich das Ergebnis an...
>>>
```

Versuchen Sie, die `cost()`-Methode direkt über das Wörterbuch aufzurufen:

```python
>>> SimpleStock.__dict__['cost'](goog)
49010.00
>>> SimpleStock.__dict__['cost'](ibm)
4561.5
>>>
```

Beachten Sie, wie Sie die in der Klassendefinition definierte Funktion aufrufen und wie das `self`-Argument die Instanz erhält.

Wenn Sie einem neuen Wert zur Klasse hinzufügen, wird dies zu einer Klassenvariablen, die für alle Instanzen sichtbar ist. Versuchen Sie es:

```python
>>> SimpleStock.spam = 42
>>> ibm.spam
42
>>> goog.spam
42
>>>
```

Beobachten Sie, dass `spam` kein Teil des Instanzwörterbuchs ist.

```python
>>> ibm.__dict__
... schauen Sie sich das Ergebnis an...
>>>
```

Stattdessen ist es Teil des Klassenwörterbuchs:

```python
>>> SimpleStock.__dict__['spam']
42
>>>
```

Im Wesentlichen ist das alles, was eine Klasse wirklich ist - es ist eine Sammlung von Werten, die von Instanzen geteilt werden.
