# Ajouter une légende et des couleurs

Nous allons ajouter une légende au graphique et colorer les étiquettes de chaque axe pour qu'elles correspondent à la couleur du jeu de données correspondant à l'aide des fonctions `legend()` et `label.set_color()`.

```python
host.legend()

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right"].label.set_color(p3.get_color())
```
