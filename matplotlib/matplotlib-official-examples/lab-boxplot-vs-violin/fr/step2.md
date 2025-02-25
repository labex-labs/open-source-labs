# Générer des données

Nous allons générer quelques données de test aléatoires à l'aide de numpy.

```python
np.random.seed(19680801)
all_data = [np.random.normal(0, std, 100) for std in range(6, 10)]
```
