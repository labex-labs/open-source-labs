# Création de données fictives

Dans la deuxième étape, nous allons créer des données fictives pour les utiliser dans le graphique.

```python
# données fictives
_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

top = x + y
bottom = np.zeros_like(top)
width = depth = 1
```
