# Générer des données aléatoires

Ensuite, nous allons générer deux tableaux de données aléatoires à l'aide de NumPy. Nous utiliserons ces tableaux pour démontrer la corrélation croisée et l'auto-corrélation.

```python
np.random.seed(19680801)
x, y = np.random.randn(2, 100)
```
