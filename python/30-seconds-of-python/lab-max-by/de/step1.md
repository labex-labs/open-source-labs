# Maximum-Wert in einer Liste basierend auf einer Funktion finden

Schreiben Sie eine Funktion `max_by(lst, fn)`, die eine Liste `lst` und eine Funktion `fn` als Argumente nimmt. Die Funktion sollte jedes Element in `lst` mithilfe der bereitgestellten Funktion `fn` auf einen Wert abbilden und dann den maximalen Wert zurückgeben.

```python
def max_by(lst, fn):
  return max(map(fn, lst))
```

```python
max_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 8
```
