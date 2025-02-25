# Stylisation de la légende

Enfin, nous pouvons styliser la légende pour la rendre plus visuellement attrayante. Nous utilisons la fonction `get_frame` pour obtenir le cadre de la légende, puis la fonction `set_facecolor` pour définir la couleur d'arrière-plan du cadre.

```python
# Put a nicer background color on the legend.
legend.get_frame().set_facecolor('C0')
```
