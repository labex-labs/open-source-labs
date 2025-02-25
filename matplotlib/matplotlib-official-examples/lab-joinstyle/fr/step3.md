# Définition de JoinStyle

Nous pouvons définir le `JoinStyle` de la ligne en utilisant la méthode `set_solid_joinstyle()` de l'objet `Line2D`. Nous allons créer un nouvel objet de ligne et définir son style de jonction sur `JoinStyle.bevel`.

```python
line = ax.lines[0]
line.set_solid_joinstyle(JoinStyle.bevel)
```
