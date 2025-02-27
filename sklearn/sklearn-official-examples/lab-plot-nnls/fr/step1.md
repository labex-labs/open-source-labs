# Générer des données aléatoires

Nous allons générer quelques données aléatoires pour tester notre algorithme. Nous allons créer 200 échantillons avec 50 caractéristiques et utiliser un coefficient réel de 3 pour chaque caractéristique. Nous allons ensuite appliquer un seuil aux coefficients pour les rendre non négatifs. Enfin, nous allons ajouter du bruit aux échantillons.

```python
import numpy as np

np.random.seed(42)

n_samples, n_features = 200, 50
X = np.random.randn(n_samples, n_features)
true_coef = 3 * np.random.randn(n_features)
true_coef[true_coef < 0] = 0
y = np.dot(X, true_coef)
y += 5 * np.random.normal(size=(n_samples,))
```
