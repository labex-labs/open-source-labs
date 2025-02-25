# Crear espacios de radios y ángulos

Crearemos los espacios de radios y ángulos utilizando la función `linspace`:

```python
# Hacer espacios de radios y ángulos (el radio r=0 se omite para evitar duplicados).
radii = np.linspace(0.125, 1.0, n_radii)
angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)[..., np.newaxis]
```
