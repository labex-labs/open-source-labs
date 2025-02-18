# Création des données

Nous allons maintenant créer des données aléatoires qui contiendront des valeurs aberrantes (outliers). Nous utiliserons `numpy.random.rand` pour générer 30 nombres aléatoires, puis nous ajouterons deux valeurs aberrantes aux données.

```python
np.random.seed(19680801)

pts = np.random.rand(30)*.2
# Maintenant, créons deux points aberrants qui sont éloignés de tout le reste.
pts[[3, 14]] +=.8
```
