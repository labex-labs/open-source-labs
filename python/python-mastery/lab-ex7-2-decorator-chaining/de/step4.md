# Erstellen eines Typüberprüfungs-Decorators mit Argumenten

In den vorherigen Schritten haben wir uns mit dem `@validated`-Decorator beschäftigt. Dieser Decorator wird verwendet, um Typannotationen in Python-Funktionen zu erzwingen. Typannotationen sind eine Möglichkeit, die erwarteten Typen von Funktionsargumenten und Rückgabewerten anzugeben. Jetzt gehen wir einen Schritt weiter. Wir werden einen flexibleren Decorator erstellen, der Typangaben als Argumente akzeptieren kann. Dies bedeutet, dass wir die Typen, die wir für jedes Argument und den Rückgabewert wünschen, auf eine explizitere Weise definieren können.

## Das Ziel verstehen

Unser Ziel ist es, einen `@enforce()`-Decorator zu erstellen. Dieser Decorator ermöglicht es uns, Typbeschränkungen mithilfe von Schlüsselwortargumenten anzugeben. Hier ist ein Beispiel, wie es funktioniert:

```python
@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x + y
```

In diesem Beispiel verwenden wir den `@enforce`-Decorator, um anzugeben, dass die Argumente `x` und `y` der Funktion `add` vom Typ `Integer` sein sollten und auch der Rückgabewert vom Typ `Integer` sein sollte. Dieser Decorator verhält sich ähnlich wie unser vorheriger `@validated`-Decorator, aber er gibt uns mehr Kontrolle über die Typangaben.

## Erstellen des enforce-Decorators

1. Öffnen Sie zunächst die Datei `validate.py` in der WebIDE. Wir werden unseren neuen Decorator zu dieser Datei hinzufügen. Hier ist der Code, den wir hinzufügen werden:

```python
from functools import wraps

class Integer:
    @classmethod
    def __instancecheck__(cls, x):
        return isinstance(x, int)

def validated(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Get function annotations
        annotations = func.__annotations__
        # Check arguments against annotations
        for arg_name, arg_value in zip(func.__code__.co_varnames, args):
            if arg_name in annotations and not isinstance(arg_value, annotations[arg_name]):
                raise TypeError(f'Expected {arg_name} to be {annotations[arg_name].__name__}')

        # Run the function and get the result
        result = func(*args, **kwargs)

        # Check the return value
        if 'return' in annotations and not isinstance(result, annotations['return']):
            raise TypeError(f'Expected return value to be {annotations["return"].__name__}')

        return result
    return wrapper

def enforce(**type_specs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Check argument types
            for arg_name, arg_value in zip(func.__code__.co_varnames, args):
                if arg_name in type_specs and not isinstance(arg_value, type_specs[arg_name]):
                    raise TypeError(f'Expected {arg_name} to be {type_specs[arg_name].__name__}')

            # Run the function and get the result
            result = func(*args, **kwargs)

            # Check the return value
            if 'return_' in type_specs and not isinstance(result, type_specs['return_']):
                raise TypeError(f'Expected return value to be {type_specs["return_"].__name__}')

            return result
        return wrapper
    return decorator
```

Lassen Sie uns analysieren, was dieser Code tut. Die Klasse `Integer` wird verwendet, um einen benutzerdefinierten Typ zu definieren. Der `validated`-Decorator überprüft die Typen der Funktionsargumente und des Rückgabewerts anhand der Typannotationen der Funktion. Der `enforce`-Decorator ist der neue, den wir erstellen. Er nimmt Schlüsselwortargumente entgegen, die die Typen für jedes Argument und den Rückgabewert angeben. Innerhalb der `wrapper`-Funktion des `enforce`-Decorators überprüfen wir, ob die Typen der Argumente und des Rückgabewerts den angegebenen Typen entsprechen. Wenn nicht, werfen wir einen `TypeError`.

2. Jetzt testen wir unseren neuen `@enforce`-Decorator. Wir werden einige Testfälle ausführen, um zu sehen, ob er wie erwartet funktioniert. Hier ist der Code, um die Tests auszuführen:

```bash
cd ~/project
python3 -c "from validate import enforce, Integer

@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x + y

# This should work
print(add(2, 3))

# This should raise a TypeError
try:
    print(add('2', 3))
except TypeError as e:
    print(f'Error: {e}')

# This should raise a TypeError
try:
    @enforce(x=Integer, y=Integer, return_=Integer)
    def bad_add(x, y):
        return str(x + y)
    print(bad_add(2, 3))
except TypeError as e:
    print(f'Error: {e}')"
```

In diesem Testcode definieren wir zunächst eine `add`-Funktion mit dem `@enforce`-Decorator. Dann rufen wir die `add`-Funktion mit gültigen Argumenten auf, was ohne Fehler funktionieren sollte. Als nächstes rufen wir die `add`-Funktion mit einem ungültigen Argument auf, was einen `TypeError` auslösen sollte. Schließlich definieren wir eine `bad_add`-Funktion, die einen Wert vom falschen Typ zurückgibt, was ebenfalls einen `TypeError` auslösen sollte.

Wenn Sie diesen Testcode ausführen, sollten Sie eine Ausgabe ähnlich der folgenden sehen:

```
5
Error: Expected x to be Integer
Error: Expected return value to be Integer
```

Diese Ausgabe zeigt, dass unser `@enforce`-Decorator korrekt funktioniert. Er wirft einen `TypeError`, wenn die Typen der Argumente oder des Rückgabewerts nicht den angegebenen Typen entsprechen.

## Vergleich der beiden Ansätze

Sowohl der `@validated`- als auch der `@enforce`-Decorator erreichen dasselbe Ziel, nämlich die Erzwingung von Typbeschränkungen, aber sie tun dies auf verschiedene Weise.

1. Der `@validated`-Decorator verwendet die eingebauten Typannotationen von Python. Hier ist ein Beispiel:

   ```python
   @validated
   def add(x: Integer, y: Integer) -> Integer:
       return x + y
   ```

   Mit diesem Ansatz geben wir die Typen direkt in der Funktionsdefinition mithilfe von Typannotationen an. Dies ist ein eingebautes Feature von Python und bietet bessere Unterstützung in integrierten Entwicklungsumgebungen (IDEs). IDEs können diese Typannotationen nutzen, um Codevervollständigung, Typüberprüfung und andere nützliche Funktionen bereitzustellen.

2. Der `@enforce`-Decorator hingegen verwendet Schlüsselwortargumente, um die Typen anzugeben. Hier ist ein Beispiel:

   ```python
   @enforce(x=Integer, y=Integer, return_=Integer)
   def add(x, y):
       return x + y
   ```

   Dieser Ansatz ist expliziter, da wir die Typangaben direkt als Argumente an den Decorator übergeben. Er kann nützlich sein, wenn man mit Bibliotheken arbeitet, die auf anderen Annotationssystemen beruhen.

Jeder Ansatz hat seine eigenen Vorteile. Typannotationen sind ein nativer Bestandteil von Python und bieten bessere IDE-Unterstützung, während der `@enforce`-Ansatz uns mehr Flexibilität und Explizitheit gibt. Sie können den Ansatz wählen, der am besten zu Ihren Bedürfnissen passt, je nachdem, an welchem Projekt Sie arbeiten.
