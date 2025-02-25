# Créer un tracé pcolormesh sans rastérisation

Nous allons créer un tracé pcolormesh sans rastérisation pour illustrer la différence entre la rastérisation et la non-rastérisation.

```python
ax1.set_aspect(1)
ax1.pcolormesh(xx, yy, d)
ax1.set_title("No Rasterization")
```
