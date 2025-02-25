# Création de l'objet PathPatch

Maintenant que nous avons l'objet `Path`, nous pouvons créer l'objet `PathPatch` qui sera utilisé pour tracer la courbe de Bézier sur le tracé. Nous allons définir la couleur de fond (`facecolor`) sur `'none'` afin que seule la courbe soit tracée et non remplie.

```python
bezier_patch = mpatches.PathPatch(bezier_path, fc="none")
```
