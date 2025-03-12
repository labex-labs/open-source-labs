# Beibehalten von Funktionsmetadaten in Decorators

In Python sind Decorators (Dekorateure) ein leistungsstarkes Werkzeug, das es Ihnen ermöglicht, das Verhalten von Funktionen zu ändern. Allerdings gibt es ein kleines Problem, wenn Sie einen Decorator verwenden, um eine Funktion zu umhüllen. Standardmäßig gehen die Metadaten der ursprünglichen Funktion, wie ihr Name, ihre Dokumentationszeichenfolge (Docstring) und ihre Anmerkungen (Annotations), verloren. Metadaten sind wichtig, da sie die Introspektion (die Untersuchung der Code-Struktur) und die Generierung von Dokumentation erleichtern. Lassen Sie uns zunächst dieses Problem verifizieren.

Öffnen Sie Ihr Terminal in der WebIDE. Wir werden einige Python-Befehle ausführen, um zu sehen, was passiert, wenn wir einen Decorator verwenden. Die folgenden Befehle erstellen eine einfache Funktion `add`, die mit einem Decorator umhüllt wird, und geben dann die Funktion und ihren Docstring aus.

```bash
cd ~/project
python3 -c "from logcall import logged; @logged
def add(x,y):
    'Adds two things'
    return x+y
    
print(add)
print(add.__doc__)"
```

Wenn Sie diese Befehle ausführen, sehen Sie eine Ausgabe ähnlich dieser:

```
<function wrapper at 0x...>
None
```

Beachten Sie, dass anstelle des Funktionsnamens `add` der Name `wrapper` angezeigt wird. Und der Docstring, der `'Adds two things'` sein sollte, ist `None`. Dies kann ein großes Problem sein, wenn Sie Tools verwenden, die auf diesen Metadaten basieren, wie Introspektions-Tools oder Dokumentations-Generatoren.

## Beheben des Problems mit functools.wraps

Python's `functools`-Modul kommt uns hier zu Hilfe. Es bietet einen `wraps`-Decorator, der uns dabei helfen kann, die Funktionsmetadaten zu bewahren. Lassen Sie uns sehen, wie wir unseren `logged`-Decorator so ändern können, dass er `wraps` verwendet.

1. Öffnen Sie zunächst die Datei `logcall.py` in der WebIDE. Sie können in das Projektverzeichnis navigieren, indem Sie den folgenden Befehl im Terminal ausführen:

```bash
cd ~/project
```

2. Aktualisieren Sie nun den `logged`-Decorator in `logcall.py` mit dem folgenden Code. Der `@wraps(func)`-Decorator ist hier der Schlüssel. Er kopiert alle Metadaten von der ursprünglichen Funktion `func` auf die Wrapper-Funktion.

```python
from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

3. Der `@wraps(func)`-Decorator erledigt eine wichtige Aufgabe. Er nimmt alle Metadaten (wie den Namen, den Docstring und die Anmerkungen) von der ursprünglichen Funktion `func` und fügt sie der `wrapper`-Funktion hinzu. Auf diese Weise hat die dekorierte Funktion die richtigen Metadaten.

4. Lassen Sie uns unseren verbesserten Decorator testen. Führen Sie die folgenden Befehle im Terminal aus:

```bash
python3 -c "from logcall import logged; @logged
def add(x,y):
    'Adds two things'
    return x+y
    
print(add)
print(add.__doc__)"
```

Jetzt sollten Sie sehen:

```
<function add at 0x...>
Adds two things
```

Toll! Der Funktionsname und der Docstring werden beibehalten. Dies bedeutet, dass unser Decorator jetzt wie erwartet funktioniert und die Metadaten der ursprünglichen Funktion intakt sind.

## Beheben des Problems im validate.py-Decorator

Lassen Sie uns nun dasselbe Verfahren auf den `validated`-Decorator in `validate.py` anwenden. Dieser Decorator wird verwendet, um die Typen der Funktionsargumente und den Rückgabewert basierend auf den Anmerkungen der Funktion zu überprüfen.

1. Öffnen Sie `validate.py` in der WebIDE.

2. Aktualisieren Sie den `validated`-Decorator mit dem `@wraps`-Decorator. Der folgende Code zeigt, wie dies geht. Der `@wraps(func)`-Decorator wird der `wrapper`-Funktion innerhalb des `validated`-Decorators hinzugefügt, um die Metadaten zu bewahren.

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
```

3. Lassen Sie uns testen, ob unser `validated`-Decorator jetzt die Metadaten beibehält. Führen Sie die folgenden Befehle im Terminal aus:

```bash
python3 -c "from validate import validated, Integer; @validated
def multiply(x: Integer, y: Integer) -> Integer:
    'Multiplies two integers'
    return x * y
    
print(multiply)
print(multiply.__doc__)"
```

Sie sollten sehen:

```
<function multiply at 0......>
Multiplies two integers
```

Jetzt behalten beide Decorators, `logged` und `validated`, die Metadaten der Funktionen, die sie dekorieren, ordnungsgemäß bei. Dies stellt sicher, dass die Funktionen, wenn Sie diese Decorators verwenden, immer noch ihre ursprünglichen Namen, Docstrings und Anmerkungen haben, was für die Lesbarkeit und Wartbarkeit des Codes sehr nützlich ist.
