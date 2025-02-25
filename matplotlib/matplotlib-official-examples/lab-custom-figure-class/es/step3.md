# Crear datos para la trama

Cree algunos datos para la trama. En este ejemplo, crearemos los arrays `x` e `y` utilizando la biblioteca `numpy`.

```python
x = np.linspace(-3, 3, 201)
y = np.tanh(x) + 0.1 * np.cos(5 * x)
```
