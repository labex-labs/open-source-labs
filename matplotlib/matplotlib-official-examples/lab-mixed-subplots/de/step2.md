# Funktionen definieren

In diesem Schritt werden wir eine Funktion definieren, die eine gedämpfte Schwingung erzeugt.

```python
def f(t):
    return np.cos(2*np.pi*t) * np.exp(-t)
```
