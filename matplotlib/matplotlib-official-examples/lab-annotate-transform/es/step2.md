# Crear datos

A continuación, crearemos algunos datos para graficar. Usaremos la biblioteca `numpy` para crear una onda sinusoidal.

```python
x = np.arange(0, 10, 0.005)
y = np.exp(-x/2.) * np.sin(2*np.pi*x)
```
