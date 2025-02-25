# Générer des données

Nous allons générer quelques données aléatoires pour les utiliser dans nos exemples. Nous utiliserons la fonction `random.lognormal()` de NumPy pour générer des données log-normales avec une moyenne de 1,5 et un écart-type de 1,75. Nous allons générer 37 échantillons de 4 variables, et nous les stockerons dans la variable `data`. Nous allons également créer une liste d'étiquettes pour chaque variable.

```python
data = np.random.lognormal(size=(37, 4), mean=1.5, sigma=1.75)
labels = list('ABCD')
```
