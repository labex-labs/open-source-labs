# Crear una malla

Creamos una malla en el espacio de las variables de parametrización `u` y `v`. Esto se hace utilizando la función `np.meshgrid()` para crear una cuadrícula de puntos `u` y `v`.

```python
u = np.linspace(0, 2.0 * np.pi, endpoint=True, num=50)
v = np.linspace(-0.5, 0.5, endpoint=True, num=10)
u, v = np.meshgrid(u, v)
u, v = u.flatten(), v.flatten()
```
