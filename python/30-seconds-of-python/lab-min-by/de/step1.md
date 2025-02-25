# Finde den kleinsten Wert einer Liste basierend auf einer Funktion

Schreibe eine Funktion namens `min_by(lst, fn)`, die eine Liste `lst` und eine Funktion `fn` als Argumente nimmt. Die Funktion sollte jedes Element in der Liste mithilfe der bereitgestellten Funktion zu einem Wert abbilden und dann den kleinsten Wert zurückgeben.

```python
def min_by(lst, fn):
  return min(map(fn, lst))
```

```python
min_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 2
```
