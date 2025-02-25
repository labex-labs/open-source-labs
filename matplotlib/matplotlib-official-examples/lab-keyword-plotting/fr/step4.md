# Générer un graphique

Dans cette étape, nous allons générer un graphique en points dispersés en utilisant le dictionnaire `data` en tant qu'entrée pour la fonction `scatter()`. Nous utiliserons les chaînes de caractères correspondant aux variables `a`, `b`, `c` et `d` pour générer le graphique.

```python
fig, ax = plt.subplots()
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set(xlabel='entrée a', ylabel='entrée b')
plt.show()
```
