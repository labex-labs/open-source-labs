# Générez des données d'échantillonnage

Ensuite, nous allons générer quelques données d'échantillonnage pour les utiliser dans l'histogramme. Dans cet exemple, nous allons générer trois ensembles de données aléatoires.

```python
np.random.seed(19680801)
n_bins = 10
x = np.random.randn(1000, 3)
```
