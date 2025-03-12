# Grundlagen zu Python-Generatoren

Generatoren sind eine leistungsstarke Funktion in Python. Sie bieten eine einfache und elegante Möglichkeit, Iteratoren zu erstellen. In Python sind Iteratoren bei der Arbeit mit Datenfolgen sehr nützlich, da sie es ermöglichen, schrittweise durch eine Reihe von Werten zu iterieren. Normale Funktionen geben in der Regel einen einzelnen Wert zurück und beenden dann die Ausführung. Generatoren hingegen können über einen Zeitraum hinweg eine Folge von Werten liefern, was bedeutet, dass sie schrittweise mehrere Werte produzieren können.

## Was ist ein Generator?

Eine Generatorfunktion sieht ähnlich aus wie eine normale Funktion. Der entscheidende Unterschied liegt jedoch in der Art, wie sie Werte zurückgibt. Anstatt die `return`-Anweisung zu verwenden, um ein einzelnes Ergebnis bereitzustellen, verwendet eine Generatorfunktion die `yield`-Anweisung. Die `yield`-Anweisung ist speziell. Jedes Mal, wenn sie ausgeführt wird, wird der Zustand der Funktion angehalten, und der Wert, der auf das `yield`-Schlüsselwort folgt, wird an den Aufrufer zurückgegeben. Wenn die Generatorfunktion erneut aufgerufen wird, wird die Ausführung genau dort fortgesetzt, wo sie aufgehört hat.

Beginnen wir mit der Erstellung einer einfachen Generatorfunktion. Die integrierte `range()`-Funktion in Python unterstützt keine Bruchschritte. Wir werden daher eine Generatorfunktion erstellen, die eine Zahlenfolge mit einem Bruchschritt erzeugen kann.

1. Öffnen Sie zunächst ein neues Python-Terminal in der WebIDE. Klicken Sie dazu auf das Menü "Terminal" und wählen Sie dann "Neues Terminal".
2. Sobald das Terminal geöffnet ist, geben Sie den folgenden Code in das Terminal ein. Dieser Code definiert eine Generatorfunktion und testet sie anschließend.

```python
def frange(start, stop, step):
    current = start
    while current < stop:
        yield current
        current += step

# Test the generator with a for loop
for x in frange(0, 2, 0.25):
    print(x, end=' ')
```

In diesem Code ist die `frange`-Funktion eine Generatorfunktion. Sie initialisiert eine Variable `current` mit dem `start`-Wert. Solange `current` kleiner als der `stop`-Wert ist, gibt sie den `current`-Wert zurück und erhöht dann `current` um den `step`-Wert. Die `for`-Schleife iteriert dann über die von der `frange`-Generatorfunktion erzeugten Werte und gibt sie aus.

Sie sollten die folgende Ausgabe sehen:

```
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
```

## Die einmalige Natur von Generatoren

Eine wichtige Eigenschaft von Generatoren ist, dass sie erschöpfbar sind. Dies bedeutet, dass Sie, nachdem Sie alle von einem Generator erzeugten Werte durchlaufen haben, ihn nicht erneut verwenden können, um dieselbe Wertesequenz zu erzeugen. Wir demonstrieren dies anhand des folgenden Codes:

```python
# Create a generator object
f = frange(0, 2, 0.25)

# First iteration works fine
print("First iteration:")
for x in f:
    print(x, end=' ')
print("\n")

# Second iteration produces nothing
print("Second iteration:")
for x in f:
    print(x, end=' ')
print("\n")
```

In diesem Code erstellen wir zunächst ein Generatorobjekt `f` mithilfe der `frange`-Funktion. Die erste `for`-Schleife iteriert über alle vom Generator erzeugten Werte und gibt sie aus. Nach der ersten Iteration ist der Generator erschöpft, was bedeutet, dass er bereits alle Werte erzeugt hat, die er kann. Wenn wir also versuchen, ihn in der zweiten `for`-Schleife erneut zu durchlaufen, erzeugt er keine neuen Werte.

Ausgabe:

```
First iteration:
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75

Second iteration:

```

Beachten Sie, dass die zweite Iteration keine Ausgabe erzeugt hat, da der Generator bereits erschöpft war.

## Erstellen wiederverwendbarer Generatoren mit Klassen

Wenn Sie mehrmals über dieselbe Wertesequenz iterieren müssen, können Sie den Generator in einer Klasse verpacken. Auf diese Weise wird jedes Mal, wenn Sie eine neue Iteration starten, ein neuer Generator erstellt.

```python
class FRange:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        n = self.start
        while n < self.stop:
            yield n
            n += self.step

# Create an instance
f = FRange(0, 2, 0.25)

# We can iterate multiple times
print("First iteration:")
for x in f:
    print(x, end=' ')
print("\n")

print("Second iteration:")
for x in f:
    print(x, end=' ')
print("\n")
```

In diesem Code definieren wir eine Klasse `FRange`. Die `__init__`-Methode initialisiert die `start`-, `stop`- und `step`-Werte. Die `__iter__`-Methode ist eine spezielle Methode in Python-Klassen. Sie wird verwendet, um einen Iterator zu erstellen. Innerhalb der `__iter__`-Methode haben wir einen Generator, der Werte auf ähnliche Weise erzeugt wie die zuvor definierte `frange`-Funktion.

Wenn wir eine Instanz `f` der `FRange`-Klasse erstellen und mehrmals über sie iterieren, ruft jede Iteration die `__iter__`-Methode auf, die einen neuen Generator erstellt. So können wir dieselbe Wertesequenz mehrmals erhalten.

Ausgabe:

```
First iteration:
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75

Second iteration:
0 0.25 0.5 0.75 1.0 1.25 1.5 1.75
```

Diesmal können wir mehrmals iterieren, da die `__iter__()`-Methode jedes Mal, wenn sie aufgerufen wird, einen neuen Generator erstellt.
