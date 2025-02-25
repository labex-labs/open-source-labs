# Testen, ob jedes Listelement falsch ist

## Problem

Schreiben Sie eine Python-Funktion namens `none(lst, fn = lambda x: x)`, die eine Liste `lst` und eine optionale Funktion `fn` als Argumente nimmt. Die Funktion sollte `True` zurückgeben, wenn jedes Element in der Liste falsch ist, und `False` sonst. Wenn die optionale Funktion `fn` angegeben wird, sollte sie verwendet werden, um die Wahrheitswerte der einzelnen Elemente in der Liste zu bestimmen.

Um zu bestimmen, ob ein Element falsch ist, können Sie die gleichen Regeln wie die Python-`bool()`-Funktion verwenden. Im Allgemeinen gelten die folgenden Werte als falsch:

- `False`
- `None`
- `0` (ganzzahlig)
- `0.0` (fließkomma)
- `''` (leerer String)
- `[]` (leere Liste)
- `{}` (leeres Dictionary)
- `()` (leeres Tupel)
- `set()` (leere Menge)

Wenn die optionale Funktion `fn` angegeben wird, sollte sie ein Argument akzeptieren und einen booleschen Wert zurückgeben. Die Funktion wird für jedes Element in der Liste aufgerufen, und der Rückgabewert wird verwendet, um die Wahrheitswerte des Elements zu bestimmen.

## Beispiel

```python
assert none([0, 1, 2, 0], lambda x: x >= 2 ) == False
assert none([0, 0, 0]) == True
```
