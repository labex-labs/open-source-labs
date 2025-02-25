# Tracer avec des variables catégorielles

Matplotlib vous permet de créer des graphiques en utilisant des variables catégorielles. Créons un graphique en barres, un graphique de dispersion et un graphique en ligne avec des variables catégorielles :

```python
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)

plt.suptitle('Categorical Plotting')
plt.show()
```

Explication :

- Nous créons une liste `names` avec trois valeurs catégorielles et une liste `values` représentant leurs valeurs correspondantes.
- La fonction `figure` est appelée pour créer une nouvelle figure avec une taille spécifiée.
- Nous utilisons la fonction `subplot` pour créer une grille de sous-graphiques. Dans cet exemple, nous créons trois sous-graphiques, chacun avec un type de graphique différent : graphique en barres, graphique de dispersion et graphique en ligne.
- La fonction `suptitle` est utilisée pour définir le titre principal de la figure.
