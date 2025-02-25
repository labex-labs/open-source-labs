# Führe Funktion für jedes Listelement aus

Schreiben Sie eine Funktion `for_each(itr, fn)`, die eine Liste `itr` und eine Funktion `fn` als Argumente nimmt. Die Funktion sollte `fn` einmal für jedes Element in `itr` ausführen.

```python
def for_each(itr, fn):
  for el in itr:
    fn(el)
```

```python
for_each([1, 2, 3], print) # 1 2 3
```
