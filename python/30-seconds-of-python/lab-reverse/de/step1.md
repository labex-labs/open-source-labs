# Funktion zur Umkehrung einer Liste

Schreiben Sie eine Python-Funktion namens `reverse(itr)`, die eine Liste oder einen String als Argument nimmt und eine neue Liste oder einen String zurückgibt, der die Elemente oder Zeichen in umgekehrter Reihenfolge enthält.

Ihre Funktion sollte die folgenden Anforderungen erfüllen:

- Die Funktion sollte `reverse` heißen
- Die Funktion sollte ein einzelnes Argument akzeptieren, das eine Liste oder ein String ist
- Die Funktion sollte eine neue Liste oder einen String zurückgeben, der die Elemente oder Zeichen in umgekehrter Reihenfolge enthält
- Die Funktion sollte die ursprüngliche Liste oder den ursprünglichen String nicht modifizieren

```python
def reverse(itr):
  return itr[::-1]
```

```python
reverse([1, 2, 3]) # [3, 2, 1]
reverse('snippet') # 'teppins'
```
