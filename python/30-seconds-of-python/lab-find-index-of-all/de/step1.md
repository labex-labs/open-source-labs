# Alle passenden Indizes finden

Schreiben Sie eine Funktion `find_index_of_all(lst, fn)`, die eine Liste `lst` und eine Testfunktion `fn` als Argumente nimmt und eine Liste von Indizes aller Elemente in `lst` zurückgibt, für die `fn` `True` zurückgibt.

### Eingabe

- Eine Liste `lst` von ganzen Zahlen.
- Eine Testfunktion `fn`, die eine ganze Zahl als Eingabe nimmt und einen booleschen Wert zurückgibt.

### Ausgabe

- Eine Liste von ganzen Zahlen, die die Indizes aller Elemente in `lst` repräsentieren, für die `fn` `True` zurückgibt.

```python
def find_index_of_all(lst, fn):
  return [i for i, x in enumerate(lst) if fn(x)]
```

```python
find_index_of_all([1, 2, 3, 4], lambda n: n % 2 == 1) # [0, 2]
```
