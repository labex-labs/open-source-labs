# Generator-Pipelines

Sie können diesen Aspekt von Generatoren nutzen, um Verarbeitungs-Pipelines aufzubauen (ähnlich wie Unix-Pipes).

_producer_ → _Verarbeitung_ → _Verarbeitung_ → _Verbraucher_

Verarbeitungs-Pipelines haben einen initialen Datenproduzenten, eine Reihe von Zwischenverarbeitungsstufen und einen Endverbraucher.

**produzent** → _Verarbeitung_ → _Verarbeitung_ → _Verbraucher_

```python
def producer():
 ...
    yield item
 ...
```

Der Produzent ist typischerweise ein Generator. Obwohl es auch eine Liste oder eine andere Sequenz sein könnte. `yield` liefert Daten in die Pipeline.

_producer_ → _Verarbeitung_ → _Verarbeitung_ → **Verbraucher**

```python
def consumer(s):
    for item in s:
 ...
```

Der Verbraucher ist eine for-Schleife. Er bekommt Elemente und verarbeitet sie.

_producer_ → **Verarbeitung** → **Verarbeitung** → _Verbraucher_

```python
def processing(s):
    for item in s:
 ...
        yield newitem
 ...
```

Zwischenverarbeitungsstufen konsumieren und produzieren Elemente gleichzeitig. Sie können den Datenstrom modifizieren. Sie können auch filtern (Elemente ausschließen).

_producer_ → _Verarbeitung_ → _Verarbeitung_ → _Verbraucher_

```python
def producer():
 ...
    yield item          # liefert das Element, das von der `Verarbeitung` empfangen wird
 ...

def processing(s):
    for item in s:      # kommt vom `producer`
 ...
        yield newitem   # liefert ein neues Element
 ...

def consumer(s):
    for item in s:      # kommt von der `Verarbeitung`
 ...
```

Code, um die Pipeline aufzusetzen

```python
a = producer()
b = processing(a)
c = consumer(b)
```

Sie werden feststellen, dass die Daten sukzessive durch die verschiedenen Funktionen fließen.

Für diese Übung sollte das Programm `stocksim.py` immer noch im Hintergrund laufen. Sie werden die Funktion `follow()`, die Sie im vorherigen Abschnitt geschrieben haben, verwenden.
