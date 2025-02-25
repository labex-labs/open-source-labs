# Création de couleurs pour le tracé de surface

Dans cette étape, nous allons créer des couleurs pour le tracé de surface. Nous allons créer un tableau vide de chaînes de caractères ayant la même forme que la grille de maillage, et le remplir avec deux couleurs selon un motif d'échiquier.

```python
# Create colors for the surface plot
colortuple = ('y', 'b')
colors = np.empty(X.shape, dtype=str)
for y in range(ylen):
    for x in range(xlen):
        colors[y, x] = colortuple[(x + y) % len(colortuple)]
```
