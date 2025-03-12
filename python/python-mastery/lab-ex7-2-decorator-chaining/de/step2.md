# Erstellen von Decorators mit Argumenten

Bisher haben wir den `@logged`-Decorator verwendet, der immer eine feste Nachricht ausgibt. Aber was, wenn Sie das Nachrichtenformat anpassen möchten? In diesem Abschnitt lernen wir, wie man einen neuen Decorator erstellt, der Argumente akzeptieren kann. Dies gibt Ihnen mehr Flexibilität bei der Verwendung von Decorators.

## Verständnis von parametrisierten Decorators

Ein parametrisierter Decorator ist eine besondere Art von Funktion. Anstatt direkt eine andere Funktion zu modifizieren, gibt er einen Decorator zurück. Die allgemeine Struktur eines parametrisierten Decorators sieht wie folgt aus:

```python
def decorator_with_args(arg1, arg2, ...):
    def actual_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Use arg1, arg2, ... here
            # Call the original function
            return func(*args, **kwargs)
        return wrapper
    return actual_decorator
```

Wenn Sie `@decorator_with_args(value1, value2)` in Ihrem Code verwenden, ruft Python zunächst `decorator_with_args(value1, value2)` auf. Dieser Aufruf gibt den eigentlichen Decorator zurück, der dann auf die Funktion angewendet wird, die auf die `@`-Syntax folgt. Dieser zweistufige Prozess ist der Schlüssel für die Funktionsweise von parametrisierten Decorators.

## Erstellen des logformat-Decorators

Lassen Sie uns einen `@logformat(fmt)`-Decorator erstellen, der eine Formatzeichenfolge als Argument nimmt. Dies ermöglicht es uns, die Protokollnachricht anzupassen.

1. Öffnen Sie `logcall.py` in der WebIDE und fügen Sie den neuen Decorator hinzu. Der folgende Code zeigt, wie man sowohl den bestehenden `logged`-Decorator als auch den neuen `logformat`-Decorator definiert:

```python
from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def logformat(fmt):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

Im `logformat`-Decorator nimmt die äußere Funktion `logformat` eine Formatzeichenfolge `fmt` als Argument. Sie gibt dann die `decorator`-Funktion zurück, die der eigentliche Decorator ist, der die Ziel-Funktion modifiziert.

2. Jetzt testen wir unseren neuen Decorator, indem wir `sample.py` ändern. Der folgende Code zeigt, wie man sowohl den `logged`- als auch den `logformat`-Decorator auf verschiedene Funktionen anwendet:

```python
from logcall import logged, logformat

@logged
def add(x, y):
    "Adds two numbers"
    return x + y

@logged
def sub(x, y):
    "Subtracts y from x"
    return x - y

@logformat('{func.__code__.co_filename}:{func.__name__}')
def mul(x, y):
    "Multiplies two numbers"
    return x * y
```

Hier verwenden die Funktionen `add` und `sub` den `logged`-Decorator, während die Funktion `mul` den `logformat`-Decorator mit einer benutzerdefinierten Formatzeichenfolge verwendet.

3. Führen Sie die aktualisierte Datei `sample.py` aus, um die Ergebnisse zu sehen. Öffnen Sie Ihr Terminal und führen Sie den folgenden Befehl aus:

```bash
cd ~/project
python3 -c "import sample; print(sample.add(2, 3)); print(sample.mul(2, 3))"
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Calling add
5
sample.py:mul
6
```

Diese Ausgabe zeigt, dass der `logged`-Decorator wie erwartet den Funktionsnamen ausgibt und der `logformat`-Decorator die benutzerdefinierte Formatzeichenfolge verwendet, um den Dateinamen und den Funktionsnamen auszugeben.

## Neudefinieren des logged-Decorators unter Verwendung von logformat

Jetzt, da wir einen flexibleren `logformat`-Decorator haben, können wir unseren ursprünglichen `logged`-Decorator unter Verwendung dieses neuen Decorators neu definieren. Dies hilft uns, Code wiederzuverwenden und ein konsistentes Protokollformat beizubehalten.

1. Aktualisieren Sie `logcall.py` mit dem folgenden Code:

```python
from functools import wraps

def logformat(fmt):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Define logged using logformat
logged = lambda func: logformat("Calling {func.__name__}")(func)
```

Hier verwenden wir eine Lambda-Funktion, um den `logged`-Decorator in Bezug auf den `logformat`-Decorator zu definieren. Die Lambda-Funktion nimmt eine Funktion `func` und wendet den `logformat`-Decorator mit einer bestimmten Formatzeichenfolge an.

2. Testen Sie, ob der neu definierte `logged`-Decorator noch funktioniert. Öffnen Sie Ihr Terminal und führen Sie den folgenden Befehl aus:

```bash
cd ~/project
python3 -c "from logcall import logged; @logged
def greet(name):
    return f'Hello, {name}'
    
print(greet('World'))"
```

Sie sollten sehen:

```
Calling greet
Hello, World
```

Dies zeigt, dass der neu definierte `logged`-Decorator wie erwartet funktioniert und wir den `logformat`-Decorator erfolgreich wiederverwendet haben, um ein konsistentes Protokollformat zu erreichen.
