# Implementierung der Typüberprüfung mit Funktionsannotationen

In Python können Sie Typannotationen für Funktionsparameter hinzufügen. Diese Annotationen dienen dazu, die erwarteten Datentypen der Parameter und den Rückgabewert einer Funktion anzugeben. Standardmäßig erzwingen sie die Typen nicht zur Laufzeit, aber sie können für Validierungszwecke verwendet werden.

Schauen wir uns ein Beispiel an:

```python
def add(x: int, y: int) -> int:
    return x + y
```

In diesem Code sagen `x: int` und `y: int`, dass die Parameter `x` und `y` Ganzzahlen sein sollten. Das `-> int` am Ende gibt an, dass die Funktion `add` eine Ganzzahl zurückgibt. Diese Typannotationen werden im `__annotations__`-Attribut der Funktion gespeichert, einem Wörterbuch, das die Parameternamen auf ihre annotierten Typen abbildet.

Jetzt werden wir unsere `ValidatedFunction`-Klasse erweitern, um diese Typannotationen für die Validierung zu nutzen. Dazu müssen wir das `inspect`-Modul von Python verwenden. Dieses Modul bietet nützliche Funktionen, um Informationen über lebende Objekte wie Module, Klassen, Methoden, Funktionen usw. zu erhalten. In unserem Fall werden wir es nutzen, um die Funktionsargumente mit ihren entsprechenden Parameternamen zu verknüpfen.

Zunächst müssen wir die `ValidatedFunction`-Klasse in der Datei `validate.py` ändern. Sie können diese Datei mit dem folgenden Befehl öffnen:

```bash
code /home/labex/project/validate.py
```

Ersetzen Sie die vorhandene `ValidatedFunction`-Klasse durch die folgende verbesserte Version:

```python
import inspect

class ValidatedFunction:
    def __init__(self, func):
        self.func = func
        self.signature = inspect.signature(func)

    def __call__(self, *args, **kwargs):
        # Bind the arguments to the function parameters
        bound = self.signature.bind(*args, **kwargs)

        # Validate each argument against its annotation
        for name, val in bound.arguments.items():
            if name in self.func.__annotations__:
                # Get the validator class from the annotation
                validator = self.func.__annotations__[name]
                # Apply the validation
                validator.check(val)

        # Call the function with the validated arguments
        return self.func(*args, **kwargs)
```

Hier ist, was diese verbesserte Version tut:

1. Sie verwendet `inspect.signature()`, um Informationen über die Parameter der Funktion zu erhalten, wie ihre Namen, Standardwerte und annotierten Typen.
2. Die `bind()`-Methode der Signatur wird verwendet, um die übergebenen Argumente mit ihren entsprechenden Parameternamen zu verknüpfen. Dies hilft uns, jedes Argument mit seinem richtigen Parameter in der Funktion zu assoziieren.
3. Sie überprüft jedes Argument anhand seiner Typannotation (falls vorhanden). Wenn eine Annotation gefunden wird, ruft sie die Validator-Klasse aus der Annotation ab und wendet die Validierung mit der `check()`-Methode an.
4. Schließlich ruft sie die ursprüngliche Funktion mit den validierten Argumenten auf.

Jetzt testen wir diese verbesserte `ValidatedFunction`-Klasse mit einigen Funktionen, die unsere Validator-Klassen in ihren Typannotationen verwenden. Öffnen Sie die Datei `test_validation.py` mit dem folgenden Befehl:

```bash
code /home/labex/project/test_validation.py
```

Fügen Sie den folgenden Code zur Datei hinzu:

```python
from validate import ValidatedFunction, Integer, String

def greet(name: String, times: Integer):
    return name * times

# Wrap the greet function with ValidatedFunction
validated_greet = ValidatedFunction(greet)

# Valid call
try:
    result = validated_greet("Hello ", 3)
    print(f"Valid call result: {result}")
except TypeError as e:
    print(f"Unexpected error: {e}")

# Invalid call - wrong type for 'name'
try:
    result = validated_greet(123, 3)
    print(f"Invalid call unexpectedly succeeded: {result}")
except TypeError as e:
    print(f"Expected error for name: {e}")

# Invalid call - wrong type for 'times'
try:
    result = validated_greet("Hello ", "3")
    print(f"Invalid call unexpectedly succeeded: {result}")
except TypeError as e:
    print(f"Expected error for times: {e}")
```

In diesem Code definieren wir eine `greet`-Funktion mit den Typannotationen `name: String` und `times: Integer`. Dies bedeutet, dass der Parameter `name` mit der `String`-Klasse validiert werden sollte und der Parameter `times` mit der `Integer`-Klasse. Wir umhüllen dann die `greet`-Funktion mit unserer `ValidatedFunction`-Klasse, um die Typüberprüfung zu ermöglichen.

Wir führen drei Testfälle durch: einen gültigen Aufruf, einen ungültigen Aufruf mit dem falschen Typ für `name` und einen ungültigen Aufruf mit dem falschen Typ für `times`. Jeder Aufruf ist in einem `try-except`-Block eingeschlossen, um alle `TypeError`-Ausnahmen abzufangen, die während der Validierung auftreten können.

Um die Testdatei auszuführen, verwenden Sie den folgenden Befehl:

```bash
python3 /home/labex/project/test_validation.py
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Valid call result: Hello Hello Hello
Expected error for name: Expected <class 'str'>
Expected error for times: Expected <class 'int'>
```

Diese Ausgabe zeigt, dass unser aufrufbares `ValidatedFunction`-Objekt jetzt die Typüberprüfung basierend auf den Funktionsannotationen durchführt. Wenn wir Argumente des falschen Typs übergeben, erkennen die Validator-Klassen den Fehler und werfen einen `TypeError`. Auf diese Weise können wir sicherstellen, dass die Funktionen mit den richtigen Datentypen aufgerufen werden, was hilft, Fehler zu vermeiden und unseren Code robuster zu machen.
