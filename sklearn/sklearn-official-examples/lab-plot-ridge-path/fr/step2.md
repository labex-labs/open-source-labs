# Générer des données

Dans cette étape, nous allons générer une matrice de Hilbert 10x10 et définir la variable cible y comme étant un vecteur de uns.

```python
X = 1.0 / (np.arange(1, 11) + np.arange(0, 10)[:, np.newaxis])
y = np.ones(10)
```
