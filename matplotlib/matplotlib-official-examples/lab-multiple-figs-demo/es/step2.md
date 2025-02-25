# Crear datos

A continuación, necesitamos crear algunos datos para graficar. Crearemos dos ondas senoidales que graficaremos en figuras separadas.

```python
t = np.arange(0.0, 2.0, 0.01)
s1 = np.sin(2*np.pi*t)
s2 = np.sin(4*np.pi*t)
```
