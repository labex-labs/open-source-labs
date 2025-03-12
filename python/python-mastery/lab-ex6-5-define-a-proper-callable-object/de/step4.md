# Herausforderung: Verwenden eines aufrufbaren Objekts als Methode

In Python gibt es eine besondere Herausforderung, wenn Sie ein aufrufbares Objekt als Methode innerhalb einer Klasse verwenden. Ein aufrufbares Objekt ist etwas, das Sie wie eine Funktion "aufrufen" können, wie beispielsweise eine Funktion selbst oder ein Objekt mit einer `__call__`-Methode. Wenn es als Klassenmethode verwendet wird, funktioniert es nicht immer wie erwartet, weil Python die Instanz (`self`) als erstes Argument übergibt.

Lassen Sie uns dieses Problem untersuchen, indem wir eine `Stock`-Klasse erstellen. Diese Klasse wird eine Aktie repräsentieren, mit Attributen wie Name, Anzahl der Anteile und Preis. Wir werden auch einen Validator verwenden, um sicherzustellen, dass die Daten, mit denen wir arbeiten, korrekt sind.

Zunächst öffnen Sie die Datei `stock.py`, um unsere `Stock`-Klasse zu schreiben. Sie können den folgenden Befehl verwenden, um die Datei in einem Editor zu öffnen:

```bash
code /home/labex/project/stock.py
```

Fügen Sie jetzt den folgenden Code zur Datei `stock.py` hinzu. Dieser Code definiert die `Stock`-Klasse mit einer `__init__`-Methode, um die Attribute der Aktie zu initialisieren, einer `cost`-Eigenschaft, um die Gesamtkosten zu berechnen, und einer `sell`-Methode, um die Anzahl der Anteile zu reduzieren. Wir werden auch versuchen, die `ValidatedFunction` zu verwenden, um die Eingabe für die `sell`-Methode zu validieren.

```python
from validate import ValidatedFunction, Integer

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: Integer):
        self.shares -= nshares

    # Try to use ValidatedFunction
    sell = ValidatedFunction(sell)
```

Nachdem Sie die `Stock`-Klasse definiert haben, müssen Sie sie testen, um zu sehen, ob sie wie erwartet funktioniert. Erstellen Sie eine Testdatei namens `test_stock.py` und öffnen Sie sie mit dem folgenden Befehl:

```bash
code /home/labex/project/test_stock.py
```

Fügen Sie den folgenden Code zur Datei `test_stock.py` hinzu. Dieser Code erstellt eine Instanz der `Stock`-Klasse, gibt die anfängliche Anzahl der Anteile und die Kosten aus, versucht, einige Anteile zu verkaufen, und gibt dann die aktualisierte Anzahl der Anteile und die Kosten aus.

```python
from stock import Stock

try:
    # Create a stock
    s = Stock('GOOG', 100, 490.1)

    # Get the initial cost
    print(f"Initial shares: {s.shares}")
    print(f"Initial cost: ${s.cost}")

    # Try to sell some shares
    s.sell(10)

    # Check the updated cost
    print(f"After selling, shares: {s.shares}")
    print(f"After selling, cost: ${s.cost}")

except Exception as e:
    print(f"Error: {e}")
```

Jetzt führen Sie die Testdatei mit dem folgenden Befehl aus:

```bash
python3 /home/labex/project/test_stock.py
```

Sie werden wahrscheinlich einen Fehler ähnlich dem folgenden erhalten:

```
Error: missing a required argument: 'nshares'
```

Dieser Fehler tritt auf, weil Python, wenn es eine Methode wie `s.sell(10)` aufruft, tatsächlich `Stock.sell(s, 10)` im Hintergrund aufruft. Der `self`-Parameter repräsentiert die Instanz der Klasse und wird automatisch als erstes Argument übergeben. Allerdings behandelt unsere `ValidatedFunction` diesen `self`-Parameter nicht richtig, weil sie nicht weiß, dass sie als Methode verwendet wird.

**Das Problem verstehen**

Wenn Sie eine Methode innerhalb einer Klasse definieren und sie dann durch eine `ValidatedFunction` ersetzen, verpacken Sie im Grunde die ursprüngliche Methode. Das Problem ist, dass die verpackte Methode den `self`-Parameter nicht automatisch richtig behandelt. Sie erwartet die Argumente in einer Weise, die nicht berücksichtigt, dass die Instanz als erstes Argument übergeben wird.

**Das Problem beheben**

Um dieses Problem zu beheben, müssen wir die Art und Weise ändern, wie wir Methoden behandeln. Wir werden eine neue Klasse namens `ValidatedMethod` erstellen, die Methodenaufrufe richtig behandeln kann. Fügen Sie den folgenden Code ans Ende der Datei `validate.py` hinzu:

```python
import inspect

class ValidatedMethod:
    def __init__(self, func):
        self.func = func
        self.signature = inspect.signature(func)

    def __get__(self, instance, owner):
        # This method is called when the attribute is accessed as a method
        if instance is None:
            return self

        # Return a callable that binds 'self' to the instance
        def method_wrapper(*args, **kwargs):
            return self(instance, *args, **kwargs)

        return method_wrapper

    def __call__(self, instance, *args, **kwargs):
        # Bind the arguments to the function parameters
        bound = self.signature.bind(instance, *args, **kwargs)

        # Validate each argument against its annotation
        for name, val in bound.arguments.items():
            if name in self.func.__annotations__:
                # Get the validator class from the annotation
                validator = self.func.__annotations__[name]
                # Apply the validation
                validator.check(val)

        # Call the function with the validated arguments
        return self.func(instance, *args, **kwargs)
```

Jetzt müssen wir die `Stock`-Klasse ändern, um `ValidatedMethod` anstelle von `ValidatedFunction` zu verwenden. Öffnen Sie die Datei `stock.py` erneut:

```bash
code /home/labex/project/stock.py
```

Aktualisieren Sie die `Stock`-Klasse wie folgt:

```python
from validate import ValidatedMethod, Integer

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @ValidatedMethod
    def sell(self, nshares: Integer):
        self.shares -= nshares
```

Die `ValidatedMethod`-Klasse ist ein Descriptor, ein spezieller Objekttyp in Python, der ändern kann, wie Attribute zugegriffen werden. Die `__get__`-Methode wird aufgerufen, wenn das Attribut als Methode zugegriffen wird. Sie gibt ein aufrufbares Objekt zurück, das die Instanz korrekt als erstes Argument übergibt.

Führen Sie die Testdatei erneut mit dem folgenden Befehl aus:

```bash
python3 /home/labex/project/test_stock.py
```

Jetzt sollten Sie eine Ausgabe ähnlich der folgenden sehen:

```
Initial shares: 100
Initial cost: $49010.0
After selling, shares: 90
After selling, cost: $44109.0
```

Diese Herausforderung hat Ihnen einen wichtigen Aspekt von aufrufbaren Objekten gezeigt. Wenn Sie sie als Methoden in einer Klasse verwenden, erfordern sie eine besondere Behandlung. Indem Sie das Descriptor-Protokoll mit der `__get__`-Methode implementieren, können Sie aufrufbare Objekte erstellen, die sowohl als eigenständige Funktionen als auch als Methoden richtig funktionieren.
