# Definir funciones

Define una lista de funciones que la aplicación mostrará. Cada función está definida por un texto matemático y una función lambda que toma un valor de entrada y devuelve un valor de salida.

```python
functions = [
    (r'$\sin(2 \pi x)$', lambda x: np.sin(2*np.pi*x)),
    (r'$\frac{4}{3}\pi x^3$', lambda x: (4/3)*np.pi*x**3),
    (r'$\cos(2 \pi x)$', lambda x: np.cos(2*np.pi*x)),
    (r'$\log(x)$', lambda x: np.log(x))
]
```
