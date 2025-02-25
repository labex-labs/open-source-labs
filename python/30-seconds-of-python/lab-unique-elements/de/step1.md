# Einzigartige Elemente in einer Liste

Schreiben Sie eine Python-Funktion namens `unique_elements`, die eine Liste als Eingabe nimmt und eine neue Liste zurückgibt, die nur die einzigartigen Elemente enthält. Ihre Funktion sollte die folgenden Schritte ausführen:

- Erstellen Sie einen `Set` aus der Liste, um doppelte Werte zu entfernen.
- Geben Sie eine `Liste` aus dem Set zurück.

Ihre Funktion sollte die folgende Signatur haben:

```python
def unique_elements(li: List) -> List:
```

```python
def unique_elements(li):
  return list(set(li))
```

```python
unique_elements([1, 2, 2, 3, 4, 3]) # [1, 2, 3, 4]
```
