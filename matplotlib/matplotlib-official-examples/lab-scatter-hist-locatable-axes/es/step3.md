# Crear un diagrama de dispersión

En este paso, crearemos un diagrama de dispersión utilizando los datos aleatorios del Paso 2.

```python
fig, ax = plt.subplots(figsize=(5.5, 5.5))
ax.scatter(x, y)
ax.set_aspect(1.)
```
