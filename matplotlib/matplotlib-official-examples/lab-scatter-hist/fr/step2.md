# Générer des données aléatoires

Nous allons générer quelques données aléatoires pour les utiliser dans le graphique en nuage de points et les histogrammes.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# Generate random data
x = np.random.randn(1000)
y = np.random.randn(1000)
```
