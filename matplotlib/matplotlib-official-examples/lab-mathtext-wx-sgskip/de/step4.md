# Definieren von Funktionen

Definieren Sie eine Liste von Funktionen, die die Anwendung anzeigen wird. Jede Funktion wird durch einen Mathtext und eine Lambda-Funktion definiert, die einen Eingabewert annimmt und einen Ausgabewert zurückgibt.

```python
functions = [
    (r'$\sin(2 \pi x)$', lambda x: np.sin(2*np.pi*x)),
    (r'$\frac{4}{3}\pi x^3$', lambda x: (4/3)*np.pi*x**3),
    (r'$\cos(2 \pi x)$', lambda x: np.cos(2*np.pi*x)),
    (r'$\log(x)$', lambda x: np.log(x))
]
```
