# Créer un tracé pcolormesh avec rastérisation

Nous allons créer un tracé pcolormesh avec rastérisation pour illustrer la manière dont la rastérisation peut accélérer le rendu et produire des fichiers plus petits.

```python
ax2.set_aspect(1)
ax2.set_title("Rasterization")
ax2.pcolormesh(xx, yy, d, rasterized=True)
```
