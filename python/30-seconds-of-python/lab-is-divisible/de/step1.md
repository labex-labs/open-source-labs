# Zahl ist teilbar

Schreiben Sie eine Funktion `is_divisible(dividend, divisor)`, die zwei Integer als Argumente nimmt und `True` zurückgibt, wenn der `dividend` durch den `divisor` teilbar ist, und `False` sonst.

```python
def is_divisible(dividend, divisor):
  return dividend % divisor == 0
```

```python
is_divisible(6, 3) # True
```
