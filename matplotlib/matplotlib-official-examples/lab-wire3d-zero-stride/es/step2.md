# Crear una figura y dos subtramas

Crearemos una figura con dos subtramas utilizando el método `subplots()`. También estableceremos la proyección en `'3d'` para que nuestras subtramas sean tridimensionales.

```python
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(8, 12), subplot_kw={'projection': '3d'})
```
