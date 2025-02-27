# F-Test berechnen

Wir werden nun den F-Test-Wert für jedes Merkmal berechnen. Der F-Test erfasst nur die lineare Abhängigkeit zwischen Variablen. Wir werden die F-Test-Werte normalisieren, indem wir sie durch den maximalen F-Test-Wert dividieren.

```python
f_test, _ = f_regression(X, y)
f_test /= np.max(f_test)
```
