# Personnalisez l'apparence du graphique

Nous pouvons personnaliser davantage l'apparence de notre graphique. Suivez ces étapes :

1. Faites pivoter les étiquettes de l'axe x pour les rendre plus lisibles.

```python
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
```

2. Définissez les limites, les étiquettes et le titre des axes x et y.

```python
ax.set(xlim=[-10000, 140000],
       xlabel='Total Revenue',
       ylabel='Company',
       title='Company Revenue')
```

3. Montrez à nouveau le graphique.

```python
fig, ax = plt.subplots()
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
       title='Company Revenue')
```
