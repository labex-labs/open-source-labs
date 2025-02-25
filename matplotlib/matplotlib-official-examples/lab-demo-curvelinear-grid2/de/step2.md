# Definieren von Transformationsfunktionen

Der zweite Schritt besteht darin, die Transformationsfunktionen zu definieren. In diesem Beispiel werden wir die `tr`-Funktion verwenden, um die x-Achsenwerte zu transformieren und die y-Achsenwerte unverändert zu lassen. Die `inv_tr`-Funktion wird verwendet, um die Transformation umzukehren.

```python
def tr(x, y):
    return np.sign(x)*abs(x)**.5, y

def inv_tr(x, y):
    return np.sign(x)*x**2, y
```
