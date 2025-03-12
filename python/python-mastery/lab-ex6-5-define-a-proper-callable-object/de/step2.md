# Erstellen eines einfachen aufrufbaren Objekts

In Python ist ein aufrufbares Objekt ein Objekt, das genauso wie eine Funktion verwendet werden kann. Sie können sich vorstellen, dass Sie es "aufrufen" können, indem Sie es mit Klammern versehen, ähnlich wie Sie eine normale Funktion aufrufen. Um eine Python-Klasse wie ein aufrufbares Objekt zu machen, müssen wir eine spezielle Methode namens `__call__` implementieren. Diese Methode wird automatisch aufgerufen, wenn Sie das Objekt mit Klammern verwenden, genau wie wenn Sie eine Funktion aufrufen.

Lassen Sie uns beginnen, indem wir die Datei `validate.py` ändern. Wir werden dieser Datei eine neue Klasse namens `ValidatedFunction` hinzufügen, und diese Klasse wird unser aufrufbares Objekt sein. Um die Datei im Code-Editor zu öffnen, führen Sie den folgenden Befehl im Terminal aus:

```bash
code /home/labex/project/validate.py
```

Sobald die Datei geöffnet ist, scrollen Sie bis ans Ende und fügen Sie den folgenden Code hinzu:

```python
class ValidatedFunction:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Calling', self.func)
        result = self.func(*args, **kwargs)
        return result
```

Lassen Sie uns analysieren, was dieser Code tut. Die Klasse `ValidatedFunction` hat eine `__init__`-Methode, die der Konstruktor ist. Wenn Sie eine Instanz dieser Klasse erstellen, übergeben Sie ihr eine Funktion. Diese Funktion wird dann als Attribut der Instanz mit dem Namen `self.func` gespeichert.

Die `__call__`-Methode ist der Schlüsselteil, der diese Klasse aufrufbar macht. Wenn Sie eine Instanz der Klasse `ValidatedFunction` aufrufen, wird diese `__call__`-Methode ausgeführt. Hier ist, was sie Schritt für Schritt macht:

1. Sie gibt eine Nachricht aus, die Ihnen mitteilt, welche Funktion aufgerufen wird. Dies ist nützlich für das Debugging und das Verständnis, was passiert.
2. Sie ruft die Funktion auf, die in `self.func` gespeichert ist, mit den Argumenten, die Sie beim Aufruf der Instanz übergeben haben. Die `*args` und `**kwargs` ermöglichen es Ihnen, eine beliebige Anzahl von Positions- und Schlüsselwortargumenten zu übergeben.
3. Sie gibt das Ergebnis des Funktionsaufrufs zurück.

Jetzt testen wir diese `ValidatedFunction`-Klasse. Wir werden eine neue Datei namens `test_callable.py` erstellen, um unseren Testcode zu schreiben. Um diese neue Datei im Code-Editor zu öffnen, führen Sie den folgenden Befehl aus:

```bash
code /home/labex/project/test_callable.py
```

Fügen Sie den folgenden Code zur Datei `test_callable.py` hinzu:

```python
from validate import ValidatedFunction

def add(x, y):
    return x + y

# Wrap the add function with ValidatedFunction
validated_add = ValidatedFunction(add)

# Call the wrapped function
result = validated_add(2, 3)
print(f"Result: {result}")

# Try another call
result = validated_add(10, 20)
print(f"Result: {result}")
```

In diesem Code importieren wir zunächst die Klasse `ValidatedFunction` aus der Datei `validate.py`. Dann definieren wir eine einfache Funktion namens `add`, die zwei Zahlen nimmt und ihre Summe zurückgibt.

Wir erstellen eine Instanz der Klasse `ValidatedFunction` und übergeben ihr die Funktion `add`. Dies "umhüllt" die Funktion `add` in der Instanz der `ValidatedFunction`.

Wir rufen dann die umhüllte Funktion zweimal auf, einmal mit den Argumenten `2` und `3` und dann mit `10` und `20`. Jedes Mal, wenn wir die umhüllte Funktion aufrufen, wird die `__call__`-Methode der Klasse `ValidatedFunction` aufgerufen, die wiederum die ursprüngliche Funktion `add` aufruft.

Um den Testcode auszuführen, führen Sie den folgenden Befehl im Terminal aus:

```bash
python3 /home/labex/project/test_callable.py
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Calling <function add at 0x7f2d1c3a9940>
Result: 5
Calling <function add at 0x7f2d1c3a9940>
Result: 30
```

Diese Ausgabe zeigt, dass unser aufrufbares Objekt wie erwartet funktioniert. Wenn wir `validated_add(2, 3)` aufrufen, rufen wir tatsächlich die `__call__`-Methode der Klasse `ValidatedFunction` auf, die dann die ursprüngliche Funktion `add` aufruft.

Zurzeit gibt unsere `ValidatedFunction`-Klasse nur eine Nachricht aus und leitet den Aufruf an die ursprüngliche Funktion weiter. Im nächsten Schritt werden wir diese Klasse verbessern, um eine Typüberprüfung basierend auf den Funktionsannotationen durchzuführen.
