# Validierung (Redux)

Im letzten Übungsaufgabe hast du einen `@validated`-Dekorator geschrieben, der die Typanmerkungen durchsetzt. Beispielsweise:

```python
@validated
def add(x: Integer, y:Integer) -> Integer:
    return x + y
```

Erstelle einen neuen Dekorator `@enforce()`, der stattdessen die über Schlüsselwortargumente an den Dekorator angegebenen Typen durchsetzt. Beispielsweise:

```python
@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x + y
```

Das resultierende Verhalten der dekorierten Funktion sollte identisch sein. Hinweis: Verwende das Schlüsselwort `return_`, um den Rückgabetyp anzugeben. `return` ist ein reserviertes Wort in Python, daher musst du einen leicht anderen Namen wählen.

**Diskussion**

Das Schreiben robuster Dekoratoren ist oft viel schwieriger, als es scheint. Empfohlene Lektüre:
