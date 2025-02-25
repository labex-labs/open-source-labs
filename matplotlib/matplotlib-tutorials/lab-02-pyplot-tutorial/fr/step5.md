# Personnaliser les propriétés des lignes

Matplotlib vous permet de personnaliser diverses propriétés des lignes, telles que la largeur de la ligne, le style de tirets et la couleur. Montrez quelques façons de définir les propriétés des lignes :

```python
x = np.arange(0, 5, 0.1)
line, = plt.plot(x, np.sin(x), '-')

# Utilisation de la méthode de définition de l'instance Line2D
line.set_linewidth(2.0)  # Définir la propriété de largeur de ligne de la ligne à 2.0

# Utilisation de la fonction plt.setp
plt.setp(line, color='r', linewidth=2.0)  # Définir les propriétés de couleur et de largeur de ligne à l'aide de la fonction setp

plt.show()
```

Explication :

- Nous créons un tableau `x` et calculons les valeurs y correspondantes à l'aide de la fonction `np.sin`.
- La fonction `plot` est appelée pour créer un graphique en ligne.
- Nous utilisons la méthode `set` de l'instance `Line2D` pour définir la propriété de largeur de ligne de la ligne à 2.0.
- Alternativement, nous pouvons utiliser la fonction `setp` pour définir plusieurs propriétés de la ligne, telles que la couleur et la largeur de ligne, en utilisant des arguments clés.
