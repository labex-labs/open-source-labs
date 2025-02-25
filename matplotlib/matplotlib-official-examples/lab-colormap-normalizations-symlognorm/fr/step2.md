# Création de données synthétiques

Dans cette étape, nous allons créer un ensemble de données synthétiques composé de deux bosses, l'une négative et l'autre positive, avec l'amplitude de la bosse positive huit fois supérieure à celle de la bosse négative. Nous allons ensuite appliquer `SymLogNorm` pour visualiser les données.

```python
def rbf(x, y):
    return 1.0 / (1 + 5 * ((x ** 2) + (y ** 2)))

N = 200
gain = 8
X, Y = np.mgrid[-3:3:complex(0, N), -2:2:complex(0, N)]
Z1 = rbf(X + 0.5, Y + 0.5)
Z2 = rbf(X - 0.5, Y - 0.5)
Z = gain * Z1 - Z2

shadeopts = {'cmap': 'PRGn','shading': 'gouraud'}
colormap = 'PRGn'
lnrwidth = 0.5
```
