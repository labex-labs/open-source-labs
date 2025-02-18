# Création d'un graphique simple

Maintenant que nous avons importé Matplotlib, nous pouvons commencer à créer des visualisations. Commençons par créer un graphique simple.

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.show()
```

Ici, nous créons deux listes `x` et `y` qui contiennent les valeurs de x et de y pour notre graphique. Ensuite, nous utilisons la fonction `plot` pour créer un graphique linéaire de `x` et `y`. Enfin, nous utilisons la fonction `show` pour afficher le graphique.
