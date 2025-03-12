# Hinzufügen von Iterationsfähigkeiten zu benutzerdefinierten Klassen

Nachdem Sie die Grundlagen von Generatoren verstanden haben, werden wir diese nutzen, um Iterationsfähigkeiten zu benutzerdefinierten Klassen hinzuzufügen. In Python müssen Sie, wenn Sie eine Klasse iterierbar machen möchten, die spezielle Methode `__iter__()` implementieren. Eine iterierbare Klasse ermöglicht es Ihnen, durch ihre Elemente zu iterieren, ähnlich wie Sie durch eine Liste oder ein Tupel iterieren können. Dies ist eine leistungsstarke Funktion, die Ihre benutzerdefinierten Klassen flexibler und einfacher zu handhaben macht.

## Grundlagen zur `__iter__()`-Methode

Die `__iter__()`-Methode ist ein entscheidender Bestandteil, um eine Klasse iterierbar zu machen. Sie sollte ein Iteratorobjekt zurückgeben. Ein Iterator ist ein Objekt, über das iteriert (in einer Schleife) werden kann. Ein einfacher und effektiver Weg, dies zu erreichen, ist die Definition von `__iter__()` als Generatorfunktion. Eine Generatorfunktion verwendet das `yield`-Schlüsselwort, um nacheinander eine Folge von Werten zu produzieren. Jedes Mal, wenn die `yield`-Anweisung erreicht wird, wird die Funktion angehalten und der Wert zurückgegeben. Beim nächsten Aufruf des Iterators wird die Funktion dort fortgesetzt, wo sie aufgehört hat.

## Modifizieren der `Structure`-Klasse

In der Einrichtung für dieses Lab haben wir eine Basis-`Structure`-Klasse bereitgestellt. Andere Klassen, wie `Stock`, können von dieser `Structure`-Klasse erben. Vererbung ist eine Möglichkeit, eine neue Klasse zu erstellen, die die Eigenschaften und Methoden einer bestehenden Klasse erbt. Indem wir der `Structure`-Klasse eine `__iter__()`-Methode hinzufügen, können wir alle ihre Unterklassen iterierbar machen. Dies bedeutet, dass jede Klasse, die von `Structure` erbt, automatisch die Fähigkeit hat, in einer Schleife durchlaufen zu werden.

1. Öffnen Sie die Datei `structure.py` in der WebIDE:

```bash
cd ~/project
```

Dieser Befehl wechselt das aktuelle Arbeitsverzeichnis in das `project`-Verzeichnis, in dem sich die Datei `structure.py` befindet. Sie müssen sich im richtigen Verzeichnis befinden, um die Datei zugreifen und modifizieren zu können.

2. Betrachten Sie die aktuelle Implementierung der `Structure`-Klasse:

```python
class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, '_'+name, val)
```

Die `Structure`-Klasse hat eine `_fields`-Liste, die die Namen der Attribute speichert. Die `__init__()`-Methode ist der Konstruktor der Klasse. Sie initialisiert die Attribute des Objekts, indem sie überprüft, ob die Anzahl der übergebenen Argumente gleich der Anzahl der Felder ist. Wenn nicht, wird ein `TypeError` ausgelöst. Andernfalls werden die Attribute mit der `setattr()`-Funktion festgelegt.

3. Fügen Sie eine `__iter__()`-Methode hinzu, die nacheinander jeden Attributwert zurückgibt:

```python
def __iter__(self):
    for name in self._fields:
        yield getattr(self, name)
```

Diese `__iter__()`-Methode ist eine Generatorfunktion. Sie durchläuft die `_fields`-Liste und verwendet die `getattr()`-Funktion, um den Wert jedes Attributs zu erhalten. Das `yield`-Schlüsselwort gibt dann die Werte nacheinander zurück.

Die vollständige `structure.py`-Datei sollte jetzt wie folgt aussehen:

```python
class StructureMeta(type):
    def __new__(cls, name, bases, clsdict):
        fields = clsdict.get('_fields', [])
        for name in fields:
            clsdict[name] = property(lambda self, name=name: getattr(self, '_'+name))
        return super().__new__(cls, name, bases, clsdict)

class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, '_'+name, val)

    def __iter__(self):
        for name in self._fields:
            yield getattr(self, name)
```

Diese aktualisierte `Structure`-Klasse hat jetzt die `__iter__()`-Methode, die sie und ihre Unterklassen iterierbar macht.

4. Speichern Sie die Datei.
   Nachdem Sie die `structure.py`-Datei geändert haben, müssen Sie sie speichern, damit die Änderungen übernommen werden.

5. Testen wir nun die Iterationsfähigkeit, indem wir eine `Stock`-Instanz erstellen und über sie iterieren:

```bash
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print('Iterating over Stock:'); [print(val) for val in s]"
```

Dieser Befehl erstellt eine Instanz der `Stock`-Klasse, die von der `Structure`-Klasse erbt. Anschließend wird über die Instanz mithilfe einer Listen-Komprehension iteriert und jeder Wert ausgegeben.

Sie sollten eine Ausgabe wie diese sehen:

```
Iterating over Stock:
GOOG
100
490.1
```

Jede Klasse, die von `Structure` erbt, ist jetzt automatisch iterierbar, und die Iteration gibt die Attributwerte in der Reihenfolge zurück, die in der `_fields`-Liste definiert ist. Dies bedeutet, dass Sie problemlos durch die Attribute jeder Unterklasse von `Structure` iterieren können, ohne zusätzlichen Code für die Iteration schreiben zu müssen.
