# Crear datos

Vamos a crear algunos datos que se usarán para ilustrar el concepto de rasterización.

```python
d = np.arange(100).reshape(10, 10)  # los valores que se mapearán a colores
x, y = np.meshgrid(np.arange(11), np.arange(11))

theta = 0.25*np.pi
xx = x*np.cos(theta) - y*np.sin(theta)  # rotar x por -theta
yy = x*np.sin(theta) + y*np.cos(theta)  # rotar y por -theta
```
