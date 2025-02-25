# Créez un histogramme

Dans cette étape, nous allons créer un histogramme à l'aide de matplotlib. Nous allons définir le nombre de barres à 50 et activer le paramètre de densité pour normaliser les hauteurs des barres de sorte que l'intégrale de l'histogramme soit égale à 1.

```python
num_bins = 50
fig, ax = plt.subplots()
n, bins, patches = ax.hist(x, num_bins, density=True)
```
