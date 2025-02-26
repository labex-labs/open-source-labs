# Übung 5.3: Die Rolle von Klassen

Die Definitionen, die zu einer Klassendefinition gehören, werden von allen Instanzen dieser Klasse geteilt. Beachten Sie, dass alle Instanzen einen Link zurück zu ihrer zugehörigen Klasse haben:

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

Beachten Sie, dass der Name 'cost' weder in `goog.__dict__` noch in `ibm.__dict__` definiert ist. Stattdessen wird er von dem Klassenwörterbuch bereitgestellt. Versuchen Sie das:

```python
>>> Stock.__dict__['cost']
... schauen Sie sich das Ergebnis an...
>>>
```

Versuchen Sie, die `cost()`-Methode direkt über das Wörterbuch aufzurufen:

```python
>>> Stock.__dict__['cost'](goog)
49010.0
>>> Stock.__dict__['cost'](ibm)
4561.5
>>>
```

Beachten Sie, wie Sie die in der Klassendefinition definierte Funktion aufrufen und wie das `self`-Argument die Instanz erhält.

Versuchen Sie, einem neuen Attribut der `Stock`-Klasse hinzuzufügen:

```python
>>> Stock.foo = 42
>>>
```

Beachten Sie, wie dieses neue Attribut jetzt auf allen Instanzen erscheint:

```python
>>> goog.foo
42
>>> ibm.foo
42
>>>
```

Beachten Sie jedoch, dass es kein Teil des Instanzenwörterbuchs ist:

```python
>>> goog.__dict__
... schauen Sie sich das Ergebnis an und bemerken Sie, dass es kein 'foo'-Attribut gibt...
>>>
```

Der Grund, warum Sie das `foo`-Attribut auf Instanzen zugreifen können, ist, dass Python immer das Klassenwörterbuch überprüft, wenn es etwas auf der Instanz selbst nicht finden kann.

Hinweis: Dieser Teil der Übung veranschaulicht etwas, das als Klassenvariable bekannt ist. Nehmen Sie beispielsweise an, dass Sie eine Klasse wie diese haben:

```python
class Foo(object):
     a = 13                  # Klassenvariable
     def __init__(self,b):
         self.b = b          # Instanzvariable
```

In dieser Klasse ist die Variable `a`, die im Körper der Klasse selbst zugewiesen wird, eine "Klassenvariable". Sie wird von allen erstellten Instanzen geteilt. Beispielsweise:

```python
>>> f = Foo(10)
>>> g = Foo(20)
>>> f.a          # Überprüfen Sie die Klassenvariable (gleich für beide Instanzen)
13
>>> g.a
13
>>> f.b          # Überprüfen Sie die Instanzvariable (unterschiedlich)
10
>>> g.b
20
>>> Foo.a = 42   # Ändern Sie den Wert der Klassenvariablen
>>> f.a
42
>>> g.a
42
>>>
```
