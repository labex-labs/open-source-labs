# Summe einer Liste basierend auf einer Funktion

Schreiben Sie eine Funktion `sum_by(lst, fn)`, die eine Liste `lst` und eine Funktion `fn` als Argumente nimmt. Die Funktion sollte jedes Element der Liste mithilfe der bereitgestellten Funktion auf einen Wert abbilden und die Summe der Werte zurückgeben.

```python
def sum_by(lst, fn):
  return sum(map(fn, lst))
```

```python
sum_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 20
```
