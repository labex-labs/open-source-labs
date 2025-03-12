# Anwenden von Decorators auf Klassenmethoden

Jetzt werden wir untersuchen, wie Decorators mit Klassenmethoden interagieren. Dies kann etwas tricky sein, da Python verschiedene Arten von Methoden hat: Instanzmethoden, Klassenmethoden, statische Methoden und Properties. Decorators sind Funktionen, die eine andere Funktion als Argument nehmen und das Verhalten dieser Funktion erweitern, ohne sie explizit zu modifizieren. Wenn wir Decorators auf Klassenmethoden anwenden, müssen wir darauf achten, wie sie mit diesen verschiedenen Methodentypen zusammenarbeiten.

## Das Problem verstehen

Lassen Sie uns sehen, was passiert, wenn wir unseren `@logged`-Decorator auf verschiedene Methodentypen anwenden. Der `@logged`-Decorator wird wahrscheinlich verwendet, um Informationen über Methodenaufrufe zu protokollieren.

1. Erstellen Sie eine neue Datei `methods.py` in der WebIDE. Diese Datei wird unsere Klasse mit verschiedenen Methodentypen enthalten, die mit dem `@logged`-Decorator dekoriert sind.

```python
from logcall import logged

class Spam:
    @logged
    def instance_method(self):
        print("Instance method called")
        return "instance result"

    @logged
    @classmethod
    def class_method(cls):
        print("Class method called")
        return "class result"

    @logged
    @staticmethod
    def static_method():
        print("Static method called")
        return "static result"

    @logged
    @property
    def property_method(self):
        print("Property method called")
        return "property result"
```

In diesem Code haben wir eine Klasse `Spam` mit vier verschiedenen Methodentypen. Jede Methode ist mit dem `@logged`-Decorator dekoriert, und einige sind auch mit anderen eingebauten Decorators wie `@classmethod`, `@staticmethod` und `@property` dekoriert.

2. Lassen Sie uns testen, wie es funktioniert. Wir werden einen Python-Befehl im Terminal ausführen, um diese Methoden aufzurufen und die Ausgabe zu sehen.

```bash
cd ~/project
python3 -c "from methods import Spam; s = Spam(); print(s.instance_method()); print(Spam.class_method()); print(Spam.static_method()); print(s.property_method)"
```

Wenn Sie diesen Befehl ausführen, werden Sie möglicherweise einige Probleme bemerken:

- Der `@property`-Decorator funktioniert möglicherweise nicht richtig mit unserem `@logged`-Decorator. Der `@property`-Decorator wird verwendet, um eine Methode als Property zu definieren, und er hat eine spezifische Arbeitsweise. Wenn er mit dem `@logged`-Decorator kombiniert wird, können Konflikte auftreten.
- Die Reihenfolge der Decorators spielt für `@classmethod` und `@staticmethod` eine Rolle. Die Reihenfolge, in der Decorators angewendet werden, kann das Verhalten der Methode ändern.

## Die Reihenfolge der Decorators

Wenn Sie mehrere Decorators anwenden, werden sie von unten nach oben angewendet. Dies bedeutet, dass der Decorator, der am nächsten an der Methodendefinition steht, zuerst angewendet wird, und dann werden die darüber liegenden nacheinander angewendet. Beispielsweise:

```python
@decorator1
@decorator2
def func():
    pass
```

Dies ist äquivalent zu:

```python
func = decorator1(decorator2(func))
```

In diesem Beispiel wird `decorator2` zuerst auf `func` angewendet, und dann wird `decorator1` auf das Ergebnis von `decorator2(func)` angewendet.

## Die Decorator-Reihenfolge korrigieren

Lassen Sie uns unsere `methods.py`-Datei aktualisieren, um die Decorator-Reihenfolge zu korrigieren. Indem wir die Reihenfolge der Decorators ändern, können wir sicherstellen, dass jede Methode wie erwartet funktioniert.

```python
from logcall import logged

class Spam:
    @logged
    def instance_method(self):
        print("Instance method called")
        return "instance result"

    @classmethod
    @logged
    def class_method(cls):
        print("Class method called")
        return "class result"

    @staticmethod
    @logged
    def static_method():
        print("Static method called")
        return "static result"

    @property
    @logged
    def property_method(self):
        print("Property method called")
        return "property result"
```

In dieser aktualisierten Version:

- Bei `instance_method` spielt die Reihenfolge keine Rolle. Instanzmethoden werden auf einer Instanz der Klasse aufgerufen, und der `@logged`-Decorator kann in beliebiger Reihenfolge angewendet werden, ohne die grundlegende Funktionalität zu beeinträchtigen.
- Bei `class_method` wenden wir `@classmethod` nach `@logged` an. Der `@classmethod`-Decorator ändert die Art und Weise, wie die Methode aufgerufen wird, und das Anwenden nach `@logged` stellt sicher, dass die Protokollierung korrekt funktioniert.
- Bei `static_method` wenden wir `@staticmethod` nach `@logged` an. Ähnlich wie bei `@classmethod` hat der `@staticmethod`-Decorator sein eigenes Verhalten, und die Reihenfolge mit dem `@logged`-Decorator muss korrekt sein.
- Bei `property_method` wenden wir `@property` nach `@logged` an. Dies stellt sicher, dass das Property-Verhalten beibehalten wird, während gleichzeitig die Protokollierungsfunktion erhalten bleibt.

3. Lassen Sie uns den aktualisierten Code testen. Wir werden den gleichen Befehl wie zuvor ausführen, um zu sehen, ob die Probleme behoben sind.

```bash
cd ~/project
python3 -c "from methods import Spam; s = Spam(); print(s.instance_method()); print(Spam.class_method()); print(Spam.static_method()); print(s.property_method)"
```

Jetzt sollten Sie für alle Methodentypen eine korrekte Protokollierung sehen:

```
Calling instance_method
Instance method called
instance result
Calling class_method
Class method called
class result
Calling static_method
Static method called
static result
Calling property_method
Property method called
property result
```

## Best Practices für Methoden-Decorators

Beim Arbeiten mit Methoden-Decorators sollten Sie die folgenden Best Practices befolgen:

1. Wenden Sie Methoden-transformierende Decorators (`@classmethod`, `@staticmethod`, `@property`) **nach** Ihren benutzerdefinierten Decorators an. Dies stellt sicher, dass die benutzerdefinierten Decorators zuerst ihre Protokollierung oder andere Operationen ausführen können, und dann können die eingebauten Decorators die Methode wie beabsichtigt transformieren.
2. Beachten Sie, dass die Ausführung der Decorators zur Klassen-Definition erfolgt, nicht zum Methoden-Aufruf. Dies bedeutet, dass jeder Setup- oder Initialisierungscode im Decorator ausgeführt wird, wenn die Klasse definiert wird, nicht wenn die Methode aufgerufen wird.
3. Bei komplexeren Fällen müssen Sie möglicherweise spezialisierte Decorators für verschiedene Methodentypen erstellen. Verschiedene Methodentypen haben unterschiedliches Verhalten, und ein "einer passt für alle"-Decorator funktioniert möglicherweise nicht in allen Situationen.
