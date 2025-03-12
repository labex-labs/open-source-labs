# Delegation als Alternative zur Vererbung

In der objektorientierten Programmierung ist das Wiederverwenden und Erweitern von Code eine häufige Aufgabe. Es gibt zwei Hauptwege, um dies zu erreichen: Vererbung und Delegation.

**Vererbung** ist ein Mechanismus, bei dem eine Unterklasse Methoden und Attribute von einer Elternklasse erbt. Die Unterklasse kann einige dieser geerbten Methoden überschreiben, um ihre eigene Implementierung bereitzustellen.

**Delegation** hingegen bedeutet, dass ein Objekt ein anderes Objekt enthält und bestimmte Methodenaufrufe an dieses weiterleitet.

In diesem Schritt werden wir die Delegation als Alternative zur Vererbung untersuchen. Wir werden eine Klasse implementieren, die einen Teil ihres Verhaltens an ein anderes Objekt delegiert.

## Einrichten eines Delegation-Beispiels

Zunächst müssen wir die Basisklasse einrichten, mit der unsere delegierende Klasse interagieren wird.

1. Erstellen Sie eine neue Datei namens `base_class.py` im Verzeichnis `/home/labex/project`. Diese Datei wird eine Klasse namens `Spam` mit drei Methoden definieren: `method_a`, `method_b` und `method_c`. Jede Methode gibt eine Nachricht aus und gibt ein Ergebnis zurück. Hier ist der Code, der in `base_class.py` eingefügt werden soll:

```python
class Spam:
    def method_a(self):
        print('Spam.method_a executed')
        return "Result from Spam.method_a"

    def method_b(self):
        print('Spam.method_b executed')
        return "Result from Spam.method_b"

    def method_c(self):
        print('Spam.method_c executed')
        return "Result from Spam.method_c"
```

Als Nächstes erstellen wir die delegierende Klasse.

2. Erstellen Sie eine neue Datei namens `delegator.py`. In dieser Datei werden wir eine Klasse namens `DelegatingSpam` definieren, die einen Teil ihres Verhaltens an eine Instanz der `Spam`-Klasse delegiert.

```python
from base_class import Spam

class DelegatingSpam:
    def __init__(self):
        # Create an instance of Spam that we'll delegate to
        self._spam = Spam()

    def method_a(self):
        # Override method_a but also call the original
        print('DelegatingSpam.method_a executed')
        result = self._spam.method_a()
        return f"Modified {result}"

    def method_c(self):
        # Completely override method_c
        print('DelegatingSpam.method_c executed')
        return "Result from DelegatingSpam.method_c"

    def __getattr__(self, name):
        # For any other attribute/method, delegate to self._spam
        print(f"Delegating {name} to the wrapped Spam object")
        return getattr(self._spam, name)
```

In der `__init__`-Methode erstellen we eine Instanz der `Spam`-Klasse. Die `method_a`-Methode überschreibt die ursprüngliche Methode, ruft aber auch die `method_a` der `Spam`-Klasse auf. Die `method_c`-Methode überschreibt die ursprüngliche Methode vollständig. Die `__getattr__`-Methode ist eine spezielle Methode in Python, die aufgerufen wird, wenn auf ein Attribut oder eine Methode zugegriffen wird, die in der `DelegatingSpam`-Klasse nicht existiert. Sie leitet dann den Aufruf an die `Spam`-Instanz weiter.

Jetzt erstellen wir eine Testdatei, um unsere Implementierung zu überprüfen.

3. Erstellen Sie eine Testdatei namens `test_delegation.py`. Diese Datei wird eine Instanz der `DelegatingSpam`-Klasse erstellen und ihre Methoden aufrufen.

```python
from delegator import DelegatingSpam

# Create a delegating object
spam = DelegatingSpam()

print("Calling method_a (overridden with delegation):")
result_a = spam.method_a()
print(f"Result: {result_a}\n")

print("Calling method_b (not defined in DelegatingSpam, delegated):")
result_b = spam.method_b()
print(f"Result: {result_b}\n")

print("Calling method_c (completely overridden):")
result_c = spam.method_c()
print(f"Result: {result_c}\n")

# Try accessing a non-existent method
try:
    print("Calling non-existent method_d:")
    spam.method_d()
except AttributeError as e:
    print(f"Error: {e}")
```

Schließlich führen wir das Testskript aus.

4. Führen Sie das Testskript mit den folgenden Befehlen im Terminal aus:

```bash
cd /home/labex/project
python3 test_delegation.py
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Calling method_a (overridden with delegation):
DelegatingSpam.method_a executed
Spam.method_a executed
Result: Modified Result from Spam.method_a

Calling method_b (not defined in DelegatingSpam, delegated):
Delegating method_b to the wrapped Spam object
Spam.method_b executed
Result: Result from Spam.method_b

Calling method_c (completely overridden):
DelegatingSpam.method_c executed
Result: Result from DelegatingSpam.method_c

Calling non-existent method_d:
Delegating method_d to the wrapped Spam object
Error: 'Spam' object has no attribute 'method_d'
```

## Delegation vs. Vererbung

Jetzt vergleichen wir die Delegation mit der traditionellen Vererbung.

1. Erstellen Sie eine Datei namens `inheritance_example.py`. In dieser Datei werden wir eine Klasse namens `InheritingSpam` definieren, die von der `Spam`-Klasse erbt.

```python
from base_class import Spam

class InheritingSpam(Spam):
    def method_a(self):
        # Override method_a but also call the parent method
        print('InheritingSpam.method_a executed')
        result = super().method_a()
        return f"Modified {result}"

    def method_c(self):
        # Completely override method_c
        print('InheritingSpam.method_c executed')
        return "Result from InheritingSpam.method_c"
```

Die `InheritingSpam`-Klasse überschreibt die `method_a` und `method_c` Methoden. In der `method_a`-Methode verwenden wir `super()`, um die `method_a` der Elternklasse aufzurufen.

Als Nächstes erstellen wir eine Testdatei für das Vererbungsbeispiel.

2. Erstellen Sie eine Testdatei namens `test_inheritance.py`. Diese Datei wird eine Instanz der `InheritingSpam`-Klasse erstellen und ihre Methoden aufrufen.

```python
from inheritance_example import InheritingSpam

# Create an inheriting object
spam = InheritingSpam()

print("Calling method_a (overridden with super call):")
result_a = spam.method_a()
print(f"Result: {result_a}\n")

print("Calling method_b (inherited from parent):")
result_b = spam.method_b()
print(f"Result: {result_b}\n")

print("Calling method_c (completely overridden):")
result_c = spam.method_c()
print(f"Result: {result_c}\n")

# Try accessing a non-existent method
try:
    print("Calling non-existent method_d:")
    spam.method_d()
except AttributeError as e:
    print(f"Error: {e}")
```

Schließlich führen wir den Vererbungstest aus.

3. Führen Sie den Vererbungstest mit den folgenden Befehlen im Terminal aus:

```bash
cd /home/labex/project
python3 test_inheritance.py
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Calling method_a (overridden with super call):
InheritingSpam.method_a executed
Spam.method_a executed
Result: Modified Result from Spam.method_a

Calling method_b (inherited from parent):
Spam.method_b executed
Result: Result from Spam.method_b

Calling method_c (completely overridden):
InheritingSpam.method_c executed
Result: Result from InheritingSpam.method_c

Calling non-existent method_d:
Error: 'InheritingSpam' object has no attribute 'method_d'
```

## Wichtige Unterschiede und Überlegungen

Schauen wir uns die Gemeinsamkeiten und Unterschiede zwischen Delegation und Vererbung an.

1. **Methodenüberschreibung**: Sowohl Delegation als auch Vererbung ermöglichen es Ihnen, Methoden zu überschreiben, aber die Syntax ist unterschiedlich.

   - Bei der Delegation definieren Sie Ihre eigene Methode und entscheiden, ob Sie die Methode des umwickelten Objekts aufrufen möchten.
   - Bei der Vererbung definieren Sie Ihre eigene Methode und verwenden `super()`, um die Methode der Elternklasse aufzurufen.

2. **Methodenzugriff**:

   - Bei der Delegation werden undefinierte Methoden über die `__getattr__`-Methode weitergeleitet.
   - Bei der Vererbung werden undefinierte Methoden automatisch geerbt.

3. **Typbeziehungen**:

   - Bei der Delegation gibt `isinstance(delegating_spam, Spam)` `False` zurück, da das `DelegatingSpam`-Objekt keine Instanz der `Spam`-Klasse ist.
   - Bei der Vererbung gibt `isinstance(inheriting_spam, Spam)` `True` zurück, da die `InheritingSpam`-Klasse von der `Spam`-Klasse erbt.

4. **Einschränkungen**: Die Delegation über `__getattr__` funktioniert nicht mit speziellen Methoden wie `__getitem__`, `__len__` usw. Diese Methoden müssten in der delegierenden Klasse explizit definiert werden.

Delegation ist besonders nützlich in folgenden Situationen:

- Sie möchten das Verhalten eines Objekts anpassen, ohne seine Hierarchie zu beeinflussen.
- Sie möchten Verhaltensweisen aus mehreren Objekten kombinieren, die keine gemeinsame Elternklasse haben.
- Sie benötigen mehr Flexibilität als die Vererbung bietet.

Vererbung wird im Allgemeinen bevorzugt, wenn:

- Die "ist-ein"-Beziehung klar ist (z.B. ein Auto ist ein Fahrzeug).
- Sie die Typkompatibilität in Ihrem Code aufrechterhalten müssen.
- Spezielle Methoden geerbt werden müssen.
