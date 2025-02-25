# Jedes n-te Element in einer Liste

Schreiben Sie eine Funktion `every_nth(lst, nth)`, die eine Liste `lst` und eine Ganzzahl `nth` als Argumente nimmt und eine neue Liste zurückgibt, die jedes `n-te` Element der ursprünglichen Liste enthält.

```python
def every_nth(lst, nth):
  return lst[nth - 1::nth]
```

```python
every_nth([1, 2, 3, 4, 5, 6], 2) # [ 2, 4, 6 ]
```
