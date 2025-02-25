# Definir funciones

En este paso, definiremos una función que genere una oscilación amortiguada.

```python
def f(t):
    return np.cos(2*np.pi*t) * np.exp(-t)
```
