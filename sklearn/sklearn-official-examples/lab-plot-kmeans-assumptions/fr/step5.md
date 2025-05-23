# Modèle de mélange gaussien

Nous allons explorer l'utilisation du Modèle de mélange gaussien, qui peut gérer les distributions anisotropes et les variances inégales. Dans le bloc de code suivant, nous utilisons `GaussianMixture` pour classifier les deuxième et troisième ensembles de données.

```python
from sklearn.mixture import GaussianMixture

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

y_pred = GaussianMixture(n_components=3).fit_predict(X_aniso)
ax1.scatter(X_aniso[:, 0], X_aniso[:, 1], c=y_pred)
ax1.set_title("Anisotropically Distributed Blobs")

y_pred = GaussianMixture(n_components=3).fit_predict(X_varied)
ax2.scatter(X_varied[:, 0], X_varied[:, 1], c=y_pred)
ax2.set_title("Unequal Variance")

plt.suptitle("Gaussian mixture clusters").set_y(0.95)
plt.show()
```
