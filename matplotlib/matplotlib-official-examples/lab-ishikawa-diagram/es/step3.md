# Crear el diagrama de hueso de pez

Ahora crearemos el diagrama de hueso de pez. Comenzaremos creando un objeto de figura y eje.

```python
fig, ax = plt.subplots(figsize=(10, 6), layout='constrained')
```

Luego, estableceremos los límites x e y del eje y desactivaremos el eje.

```python
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.axis('off')
```
