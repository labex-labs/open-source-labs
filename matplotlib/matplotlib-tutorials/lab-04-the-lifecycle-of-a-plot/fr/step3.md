# Créez le graphique

Nous utiliserons la visualisation en graphique à barres pour représenter les données de ventes. Suivez ces étapes :

1. Créez une figure et un objet axe à l'aide de `plt.subplots()`.

```python
fig, ax = plt.subplots()
```

2. Tracez les données à l'aide de la méthode `barh()` de l'objet axe.

```python
ax.barh(group_names, group_data)
```
