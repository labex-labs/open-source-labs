# Argumentübergabe

Wenn Sie eine Funktion aufrufen, sind die Argumentvariablen Namen, die auf die übergebenen Werte verweisen. Diese Werte sind KEINE Kopien. Wenn veränderbare Datentypen übergeben werden (z.B. Listen, Dictonaries), können sie _in-place_ geändert werden.

```python
def foo(items):
    items.append(42)    # Modifiziert das Eingabeelement

a = [1, 2, 3]
foo(a)
print(a)                # [1, 2, 3, 42]
```

**Wichtiger Punkt: Funktionen erhalten keine Kopie der Eingabeargumente.**
