# Dictionary-Werte kombinieren

## Problem

Schreiben Sie eine Funktion `combine_values(*dicts)`, die zwei oder mehr Dictionaries als Argumente nimmt und ein neues Dictionary zurückgibt, das die Werte der Eingabedictionaries kombiniert. Die Funktion sollte die folgenden Schritte ausführen:

1. Erstellen Sie ein neues `collections.defaultdict` mit `list` als Standardwert für jeden Schlüssel.
2. Iterieren Sie über die Eingabedictionaries und für jedes Dictionary:
   - Iterieren Sie über die Schlüssel des Dictionaries.
   - Fügen Sie den Wert des Schlüssels zur Liste der Werte für diesen Schlüssel im `defaultdict` hinzu.
3. Konvertieren Sie das `defaultdict` in ein reguläres Dictionary mit der `dict()`-Funktion.
4. Geben Sie das resultierende Dictionary zurück.

Die Funktion sollte folgende Signatur haben:

```python
def combine_values(*dicts):
    pass
```

## Beispiel

```python
d1 = {'a': 1, 'b': 'foo', 'c': 400}
d2 = {'a': 3, 'b': 200, 'd': 400}

combine_values(d1, d2) # {'a': [1, 3], 'b': ['foo', 200], 'c': [400], 'd': [400]}
```
