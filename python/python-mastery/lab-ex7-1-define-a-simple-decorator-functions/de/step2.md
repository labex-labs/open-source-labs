# Erstellen eines Validierungs-Decorators

In diesem Schritt werden wir einen praktischeren Decorator erstellen. Ein Decorator in Python ist eine spezielle Art von Funktion, die das Verhalten einer anderen Funktion ändern kann. Der von uns zu erstellende Decorator wird die Funktionsargumente anhand von Typannotationen validieren. Typannotationen sind eine Möglichkeit, die erwarteten Datentypen der Argumente und des Rückgabewerts einer Funktion anzugeben. Dies ist ein häufiger Anwendungsfall in realen Anwendungen, da es hilft sicherzustellen, dass Funktionen die richtigen Eingabetypen erhalten, was viele Fehler vermeiden kann.

## Verständnis der Validierungsklassen

Wir haben bereits eine Datei namens `validate.py` für Sie erstellt, die einige Validierungsklassen enthält. Validierungsklassen werden verwendet, um zu prüfen, ob ein Wert bestimmte Kriterien erfüllt. Um sehen zu können, was in dieser Datei enthalten ist, müssen Sie sie im VSCode-Editor öffnen. Sie können dies tun, indem Sie die folgenden Befehle im Terminal ausführen:

```bash
cd /home/labex/project
code validate.py
```

Die Datei enthält drei Klassen:

1. `Validator` - Dies ist eine Basisklasse. Eine Basisklasse bietet ein allgemeines Gerüst oder eine Struktur, von der andere Klassen erben können. In diesem Fall bietet sie die grundlegende Struktur für die Validierung.
2. `Integer` - Diese Validator-Klasse wird verwendet, um sicherzustellen, dass ein Wert eine Ganzzahl ist. Wenn Sie einem Funktionsaufruf, der diesen Validator verwendet, einen Wert übergeben, der keine Ganzzahl ist, wird ein Fehler ausgelöst.
3. `PositiveInteger` - Diese Validator-Klasse stellt sicher, dass ein Wert eine positive Ganzzahl ist. Wenn Sie also eine negative Ganzzahl oder Null übergeben, wird ebenfalls ein Fehler ausgelöst.

## Hinzufügen des Validierungs-Decorators

Jetzt werden wir der Datei `validate.py` eine Decorator-Funktion namens `validated` hinzufügen. Dieser Decorator wird mehrere wichtige Aufgaben ausführen:

1. Er wird die Typannotationen einer Funktion untersuchen. Typannotationen sind wie kleine Hinweise, die uns sagen, welche Art von Daten die Funktion erwartet.
2. Er wird die an die Funktion übergebenen Argumente anhand dieser Typannotationen validieren. Das bedeutet, er wird prüfen, ob die an die Funktion übergebenen Werte vom richtigen Typ sind.
3. Er wird auch den Rückgabewert der Funktion anhand seiner Annotation validieren. Somit wird sichergestellt, dass die Funktion den Datentyp zurückgibt, den sie zurückgeben soll.
4. Wenn die Validierung fehlschlägt, wird er informative Fehlermeldungen ausgeben. Diese Meldungen werden Ihnen genau sagen, was schief gelaufen ist, z. B. welches Argument den falschen Typ hatte.

Fügen Sie den folgenden Code ans Ende der Datei `validate.py` hinzu:

```python
# Add to validate.py

import inspect
import functools

def validated(func):
    sig = inspect.signature(func)

    print(f'Validating {func.__name__} {sig}')

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Bind arguments to the signature
        bound = sig.bind(*args, **kwargs)
        errors = []

        # Validate each argument
        for name, value in bound.arguments.items():
            if name in sig.parameters:
                param = sig.parameters[name]
                if param.annotation != inspect.Parameter.empty:
                    try:
                        # Create an instance of the validator and validate the value
                        if isinstance(param.annotation, type) and issubclass(param.annotation, Validator):
                            validator = param.annotation()
                            bound.arguments[name] = validator.validate(value)
                    except Exception as e:
                        errors.append(f'    {name}: {e}')

        # If validation errors, raise an exception
        if errors:
            raise TypeError('Bad Arguments\n' + '\n'.join(errors))

        # Call the function
        result = func(*bound.args, **bound.kwargs)

        # Validate the return value
        if sig.return_annotation != inspect.Signature.empty:
            try:
                if isinstance(sig.return_annotation, type) and issubclass(sig.return_annotation, Validator):
                    validator = sig.return_annotation()
                    result = validator.validate(result)
            except Exception as e:
                raise TypeError(f'Bad return: {e}') from None

        return result

    return wrapper
```

Dieser Code verwendet das `inspect`-Modul von Python. Das `inspect`-Modul ermöglicht es uns, Informationen über lebende Objekte wie Funktionen zu erhalten. Hier verwenden wir es, um die Signatur der Funktion zu untersuchen und die Argumente anhand von Typannotationen zu validieren. Wir verwenden auch `functools.wraps`. Dies ist eine Hilfsfunktion, die die Metadaten der ursprünglichen Funktion, wie ihren Namen und ihre Docstring, beibehält. Metadaten sind wie zusätzliche Informationen über die Funktion, die uns helfen, zu verstehen, was sie tut.

## Testen des Validierungs-Decorators

Lassen Sie uns eine Datei erstellen, um unseren Validierungs-Decorator zu testen. Wir werden eine neue Datei namens `test_validate.py` erstellen und den folgenden Code hinzufügen:

```python
# test_validate.py

from validate import Integer, PositiveInteger, validated

@validated
def add(x: Integer, y: Integer) -> Integer:
    return x + y

@validated
def pow(x: Integer, y: Integer) -> Integer:
    return x ** y

# Test with a class
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @validated
    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

Jetzt werden wir unseren Decorator im Python-Interpreter testen. Navigieren Sie zunächst in das Projektverzeichnis und starten Sie den Python-Interpreter, indem Sie die folgenden Befehle im Terminal ausführen:

```bash
cd /home/labex/project
python3
```

Dann können wir im Python-Interpreter den folgenden Code ausführen, um unseren Decorator zu testen:

```python
>>> from test_validate import add, pow, Stock
Validating add (x: validate.Integer, y: validate.Integer) -> validate.Integer
Validating pow (x: validate.Integer, y: validate.Integer) -> validate.Integer
Validating sell (self, nshares: validate.PositiveInteger) -> <class 'inspect._empty'>
>>>
>>> # Test with valid inputs
>>> add(2, 3)
5
>>>
>>> # Test with invalid inputs
>>> add('2', '3')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/labex/project/validate.py", line 75, in wrapper
    raise TypeError('Bad Arguments\n' + '\n'.join(errors))
TypeError: Bad Arguments
    x: Expected <class 'int'>
    y: Expected <class 'int'>
>>>
>>> # Test valid power
>>> pow(2, 3)
8
>>>
>>> # Test with negative exponent (produces non - integer result)
>>> pow(2, -1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/labex/project/validate.py", line 83, in wrapper
    raise TypeError(f'Bad return: {e}') from None
TypeError: Bad return: Expected <class 'int'>
>>>
>>> # Test with a class
>>> s = Stock("GOOG", 100, 490.1)
>>> s.sell(50)
>>> s.shares
50
>>>
>>> # Test with invalid shares
>>> s.sell(-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/labex/project/validate.py", line 75, in wrapper
    raise TypeError('Bad Arguments\n' + '\n'.join(errors))
TypeError: Bad Arguments
    nshares: Expected value > 0
>>> exit()
```

Wie Sie sehen können, hat unser `validated`-Decorator die Typüberprüfung von Funktionsargumenten und Rückgabewerten erfolgreich durchgeführt. Dies ist sehr nützlich, da es unseren Code robuster macht. Anstatt zuzulassen, dass Typfehler tiefer in den Code vordringen und schwer zu findende Fehler verursachen, fangen wir sie an den Funktionsgrenzen ab.
