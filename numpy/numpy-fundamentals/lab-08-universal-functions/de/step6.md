# Überschreiben des Ufunc-Verhaltens

Klassen, einschließlich von ndarray-Unterklassen, können das Verhalten von Ufuncs bei der Ausführung auf ihnen überschreiben, indem sie bestimmte spezielle Methoden definieren. Dadurch ist eine Anpassung des Ufunc-Verhaltens möglich. Schauen wir uns ein Beispiel an.

```python
import numpy as np

# Definieren Sie eine benutzerdefinierte Klasse
class MyArray(np.ndarray):
    def __add__(self, other):
        print("Benutzerdefinierte Additionsmethode aufgerufen")
        return super().__add__(other)

# Erstellen Sie eine Instanz der benutzerdefinierten Klasse
arr = MyArray([1, 2, 3])

# Führen Sie eine Addition durch
result = arr + 1

# Drucken Sie das Ergebnis
print(result)
```

Ausgabe:

```
Benutzerdefinierte Additionsmethode aufgerufen
[2 3 4]
```
