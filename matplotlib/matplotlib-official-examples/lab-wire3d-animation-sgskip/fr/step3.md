# Créer une grille de maillage

La troisième étape consiste à créer une grille de maillage à l'aide de `linspace`.

```python
xs = np.linspace(-1, 1, 50)
ys = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(xs, ys)
```
