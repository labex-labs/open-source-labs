# Générez un jeu de données d'exemple

L'étape suivante consiste à générer un jeu de données d'exemple, qui est une droite avec du bruit gaussien. Nous utiliserons `numpy` pour générer ce jeu de données.

```python
# Générez un jeu de données d'exemple, il s'agit simplement d'une droite avec du bruit gaussien :
xmin, xmax = -5, 5
n_samples = 100
np.random.seed(0)
X = np.random.normal(size=n_samples)
y = (X > 0).astype(float)
X[X > 0] *= 4
X += 0.3 * np.random.normal(size=n_samples)

X = X[:, np.newaxis]
```
