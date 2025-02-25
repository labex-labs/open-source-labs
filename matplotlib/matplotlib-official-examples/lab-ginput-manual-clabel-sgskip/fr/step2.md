# Tracer des lignes de niveau selon la distance aux coins du triangle

Dans cette étape, nous allons tracer des lignes de niveau selon la distance aux coins du triangle. Nous allons définir une fonction de distance à partir de points individuels et tracer des lignes de niveau selon cette fonction.

```python
# Définir une fonction agréable de distance à partir de points individuels
def f(x, y, pts):
    z = np.zeros_like(x)
    for p in pts:
        z = z + 1/(np.sqrt((x - p[0])**2 + (y - p[1])**2))
    return 1/z

X, Y = np.meshgrid(np.linspace(-1, 1, 51), np.linspace(-1, 1, 51))
Z = f(X, Y, pts)

CS = plt.contour(X, Y, Z, 20)

tellme('Utilisez la souris pour sélectionner les emplacements des étiquettes de ligne de niveau, appuyez sur le bouton central pour terminer')
CL = plt.clabel(CS, manual=True)
```
