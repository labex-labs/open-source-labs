# Binomischer Koeffizient

Schreiben Sie eine Funktion namens `binomial_coefficient(n, k)`, die zwei ganze Zahlen `n` und `k` entgegennimmt und den binomischen Koeffizienten von `n` und `k` zurückgibt. Ihre Funktion sollte die `math.comb()`-Methode verwenden, um den binomischen Koeffizienten zu berechnen.

```python
from math import comb

def binomial_coefficient(n, k):
  return comb(n, k)
```

```python
binomial_coefficient(8, 2) # 28
```
