# Sammlung ist leer

## Problem

Schreiben Sie eine Python-Funktion namens `is_empty(val)`, die einen Wert als Parameter nimmt und `True` zurückgibt, wenn der Wert eine leere Sequenz oder Sammlung ist, und `False` sonst.

Um zu überprüfen, ob eine Sequenz oder Sammlung leer ist, können Sie den `not`-Operator verwenden, um den Wahrheitswert der bereitgestellten Sequenz oder Sammlung zu testen. Wenn die Sequenz oder Sammlung leer ist, wird der `not`-Operator `True` zurückgeben.

Ihre Funktion sollte in der Lage sein, die folgenden Arten von Sequenzen und Sammlungen zu verarbeiten:

- Listen
- Tupel
- Mengen
- Wörterbücher
- Zeichenketten
- Bereiche

## Beispiel

```python
assert is_empty([]) == True
assert is_empty({}) == True
assert is_empty('') == True
assert is_empty(set()) == True
assert is_empty(range(0)) == True
assert is_empty([1, 2]) == False
assert is_empty({'a': 1, 'b': 2}) == False
assert is_empty('text') == False
assert is_empty(set([1, 2])) == False
assert is_empty(range(2)) == False
```
