# Réglez d'autres attributs du trait discontinu à l'aide de méthodes appropriées

D'autres attributs du trait discontinu peuvent également être définis à l'aide de méthodes appropriées telles que `~.Line2D.set_dash_joinstyle()`, `~.Line2D.set_dash_joinstyle()` et `~.Line2D.set_gapcolor()`. Dans cet exemple, nous utiliserons les paramètres `dashes` et `gapcolor` pour définir la séquence de traits discontinus et la couleur alternative pour `line3`.

```python
line3, = ax.plot(x, y - 0.4, dashes=[4, 4], gapcolor='tab:pink',
                 label='Using the dashes and gapcolor parameters')
```
