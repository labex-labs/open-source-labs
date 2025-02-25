# Générez les données de l'histogramme

Maintenant que nous avons nos données aléatoires, nous pouvons générer un histogramme à l'aide de numpy. Nous utiliserons 50 barres pour créer notre histogramme. Ajoutez le code suivant :

```python
n, bins = np.histogram(data, 50)
```
