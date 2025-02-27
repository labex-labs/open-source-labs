# Comparez les résultats

Comparez les résultats des différents algorithmes d'apprentissage sur variété. Visualisez les données transformées pour voir comment les algorithmes ont conservé la structure sous-jacente des données.

```python
import matplotlib.pyplot as plt

# Crée un graphique en points dispersés des données transformées
plt.scatter(X_transformed[:, 0], X_transformed[:, 1], c=y)
plt.title('Apprentissage sur variété')
plt.xlabel('Composante 1')
plt.ylabel('Composante 2')
plt.show()
```
