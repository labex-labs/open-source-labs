# Générez des données aléatoires

Nous allons générer des données aléatoires en utilisant `numpy.random.randn`. Nous allons générer 4 ensembles de données avec 12250 points chacun.

```python
np.random.seed(19680801)
stack_data = np.random.randn(4, 12250)
```
