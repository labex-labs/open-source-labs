# Générer des données

Ensuite, nous allons générer quelques données aléatoires 2D pour l'histogramme. Nous utiliserons la fonction `random.rand()` de NumPy pour générer 100 valeurs aléatoires pour les variables x et y.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

x, y = np.random.rand(2, 100) * 4
```
