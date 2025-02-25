# Générez des données aléatoires

Nous allons générer deux ensembles de données aléatoires à l'aide de la fonction `random.normal` de NumPy. Ces ensembles seront utilisés pour créer des histogrammes avec différents styles.

```python
np.random.seed(19680801)

mu_x = 200
sigma_x = 25
x = np.random.normal(mu_x, sigma_x, size=100)

mu_w = 200
sigma_w = 10
w = np.random.normal(mu_w, sigma_w, size=100)
```
