# Fakultät

Schreiben Sie eine Funktion `factorial(num)`, die eine nicht-negative ganze Zahl `num` als Argument nimmt und deren Fakultät zurückgibt. Die Funktion sollte die Fakultät mithilfe der Rekursion berechnen. Wenn `num` kleiner oder gleich `1` ist, geben Sie `1` zurück. Andernfalls geben Sie das Produkt von `num` und der Fakultät von `num - 1` zurück. Die Funktion sollte eine Ausnahme werfen, wenn `num` eine negative oder eine Gleitkommazahl ist.

```python
def factorial(num):
  if not ((num >= 0) and (num % 1 == 0)):
    raise Exception("Number can't be floating point or negative.")
  return 1 if num == 0 else num * factorial(num - 1)
```

```python
factorial(6) # 720
```
