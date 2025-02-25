# Sammlung ist leer

Schreiben Sie eine Python-Funktion namens `is_empty(val)`, die einen Wert als Parameter nimmt und `True` zurückgibt, wenn der Wert eine leere Sequenz oder Sammlung ist, und `False` sonst.

Um zu überprüfen, ob eine Sequenz oder Sammlung leer ist, können Sie den `not`-Operator verwenden, um den Wahrheitswert der bereitgestellten Sequenz oder Sammlung zu testen. Wenn die Sequenz oder Sammlung leer ist, wird der `not`-Operator `True` zurückgeben.

Ihre Funktion sollte in der Lage sein, die folgenden Arten von Sequenzen und Sammlungen zu verarbeiten:

- Listen
- Tupel
- Mengen
- Wörterbücher
- Zeichenketten
- Bereiche

```python
def is_empty(val):
  return not val
```

```python
is_empty([]) # True
is_empty({}) # True
is_empty('') # True
is_empty(set()) # True
is_empty(range(0)) # True
is_empty([1, 2]) # False
is_empty({ 'a': 1, 'b': 2 }) # False
is_empty('text') # False
is_empty(set([1, 2])) # False
is_empty(range(2)) # False
```
