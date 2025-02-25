# Führe Funktion für jedes Listenelement in umgekehrter Reihenfolge aus

Schreiben Sie eine Funktion `for_each_right(itr, fn)`, die eine Liste `itr` und eine Funktion `fn` als Argumente nimmt. Die Funktion sollte `fn` einmal für jedes Element in `itr` ausführen, beginnend mit dem letzten.

```python
def for_each_right(itr, fn):
  for el in itr[::-1]:
    fn(el)
```

```python
for_each_right([1, 2, 3], print) # 3 2 1
```
